import json
from datetime import datetime, timedelta
from math import log10
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt
import numpy as np

########### GLOBALS ###########
DBM = "dBm"
COUNT = "count"
TIME = "time"
UNIT_ID = "unit_id"
SRC_MAC = "src_mac"
DST_MAC = "dst_mac"
EOF = "eof"
LINE_INDEX = "line_index"
DATA = "data"
FREQ = "frequency"
METERS = "meters"
CHANNEL = "channel"
SEQ = "seq_num"
BEACON = "beacon"
PROBE = "probe"
TYPE = "type"
HASH = "hash"
ID = "person_id"
ENABLED = "enabled"
TIME_WINDOW_MICRO_SECONDS = 500000 # which is 0.5 seconds

DEBUG_PRINT = False
USE_HASH = False
REMOVE_UNNEEDED_FIELDS_FROM_LOG_AFTER_CLUSTERING = False
########### END GLOBALS ###########

########### AUXILIARY FUNCTIONS ###########
def not_finished_merging(file_pointers_dict : dict) -> bool:
    for file_name in file_pointers_dict:
        if file_pointers_dict[file_name][EOF] == False:
            return True
    return False

def push_min_timestamp_data(logs_dict: dict, new_data : list[dict]): 
    minimum_datetime = -1
    minimum_datetime_log_index = ""
    tmp_data = ""
    for log_dict_index,log_dict in logs_dict.items():
        if log_dict[EOF] == False:
            current_index = log_dict[LINE_INDEX]
            current_index_timestamp = log_dict[DATA][current_index][TIME]
            current_datetime = datetime.fromisoformat(current_index_timestamp)
            if minimum_datetime == -1:
                minimum_datetime = current_datetime
                minimum_datetime_log_index = log_dict_index
            if current_datetime < minimum_datetime:
                minimum_datetime = current_datetime
                minimum_datetime_log_index = log_dict_index
    minimum_line_index = logs_dict[minimum_datetime_log_index][LINE_INDEX]
    new_line = logs_dict[minimum_datetime_log_index][DATA][minimum_line_index]
    new_data.append(new_line)
    logs_dict[minimum_datetime_log_index][LINE_INDEX] += 1
    if logs_dict[minimum_datetime_log_index][LINE_INDEX] == len(logs_dict[minimum_datetime_log_index][DATA]):
        logs_dict[minimum_datetime_log_index][EOF] = True

def merge_logs(logs_dict: dict, redundancy_map: dict = {}) -> list[dict]:
    """
    @ merges a list of logs into a single log, with respect to timeframe attribute per packet
    @ if a redundany mapping is supplied, will first change a group's unit id to the first id in the group
    @ for example, if a redundancy group is [1,3], the unit 3's log will change it's id to 1
    @ input needs to have in every dict a field "time"
    """
    if redundancy_map != 0:
        mapping_vector = []
        for _, val in redundancy_map.items():
            mapping_vector.append(val)
        for index, group in enumerate(mapping_vector):
            if len(group) > 1:
                for unit_log_index in group:
                    key = "unit" + str(unit_log_index)
                    if key in logs_dict and key != "unit" + str(group[0]):
                        print(key + " is now id: " + str(group[0]))
                        for packet_dict in logs_dict[key]:
                            packet_dict[UNIT_ID] = str(group[0]) # group[0] is now a representitive
    new_data = []
    tmp_logs_dict = {}
    for key, log in logs_dict.items():
        #print(key)
        index = key[len("unit"):]
        #print(key)
        #print(index)
        tmp_logs_dict[index] = {}
        tmp_logs_dict[index][DATA] = log
        tmp_logs_dict[index][EOF] = False
        tmp_logs_dict[index][LINE_INDEX] = 0
    while not_finished_merging(tmp_logs_dict):
        push_min_timestamp_data(tmp_logs_dict, new_data)
    return new_data



def dbm_2_meters(dBm: str, freq: str) -> str:
    """
    # derived from free space loss equation.
    # frequency is in MHz
    # distance is meters
    """
    if dBm is None or len(dBm) == 0:
        return -1
    dBm = float(dBm)
    freq = int(freq)
    exponent = (27.55 - (20 * log10(freq)) + abs(dBm)) / 20.0
    result = 10**exponent
    result = round(result, 2)
    return str(result)




def analyze(hash_group: list[list], threshold: int) -> list[list[str]]:
    samples_array  = hash_group[0]
    samples_labels = hash_group[1]
    packets_array  = hash_group[2]

    if len(packets_array) < 2:
        return [packets_array]

    # calculate single-linkage clustering
    linkage_calc = linkage(samples_array, method="single", metric="euclidean")

    # apply a euclidean distance threshold
    clusters_result = fcluster(linkage_calc, threshold, criterion='distance')

    # get the number of clusters calculated in conjunction to the threshold
    clusters_count = max(clusters_result)

    # Plot graph
    if DEBUG_PRINT:
        dendrogram(linkage_calc, labels=samples_labels)
        plt.title("single")
        plt.show()

    # order the labels into groups
    result_matrix = []
    for cluster_index in range(1, clusters_count + 1):
        cluster_items_indexes_array = np.where(clusters_result == cluster_index)[0]
        current_cluster = []
        for index in cluster_items_indexes_array:
            current_cluster.append(packets_array[index])
        result_matrix.append(current_cluster)
    return result_matrix


def compile_clustered_log(packet_log: list[dict], threshold: int) -> list[dict]:
    """
    @ this function will implement the single-linkage clustering 
    @ packet log should contain both probe, beacon and data packets
    @ returns a dict with a translation from mac domain to a unique identifier domain
    @ example: result["da:a1:19:8a:0e:1d"] = "102"
    """
    # map packets to lists
    probe_packets = [] # probe request
    beacon_packets = []
    data_packets = [] # ipsec / tcp / udp and other vegetebles
    for packet in packet_log:
        if packet[TYPE] == PROBE:
            probe_packets.append(packet)
        elif packet[TYPE] == BEACON:
            beacon_packets.append(packet)
        else: # TYPE == DATA
            data_packets.append(packet)

    # classify access points addresses
    access_points_macs = set()
    for packet in beacon_packets:
        access_points_macs.add(packet[SRC_MAC])

    # classify connected devices addresses
    connected_devices_macs = set()
    for packet in data_packets:
        tmp_list = [packet[SRC_MAC], packet[DST_MAC]]
        for address in tmp_list:
            if address not in access_points_macs:
                connected_devices_macs.add(address)

    # classify disconnected devices addresses
    connected_devices_packets = []
    disconnected_devices_hash_dict = {} # keys are frame body hashes, values are 3d arrays of [samples, labels, packets]
    for packet in probe_packets:
        if packet[SRC_MAC] not in connected_devices_macs:
            timestamp_float = datetime.fromisoformat(packet[TIME]).timestamp() # seconds from 1970
            sequence_number = int(packet[SEQ])
            sample_label = packet[SRC_MAC]
            if USE_HASH:
                hash_key = packet[HASH] # not implemented, right now all hashes = "0"
            else:
                hash_key = "NOHASH"
            if hash_key not in disconnected_devices_hash_dict:
                disconnected_devices_hash_dict[hash_key] = [[], [], []] # a 3xN array
            disconnected_devices_hash_dict[hash_key][0].append([timestamp_float, sequence_number]) # 2d space for clustering
            disconnected_devices_hash_dict[hash_key][1].append(sample_label) # name of src address
            disconnected_devices_hash_dict[hash_key][2].append(packet) # the packet
        else: # connected device probe request
            connected_devices_packets.append(packet)

    # debug print
    if DEBUG_PRINT:
        for key, val in disconnected_devices_hash_dict.items():
            print("hash key: " + str(key))
            for index, item in enumerate(val[1]):
                print("\t" + str(item) + " value: " + str(val[0][index]))
    # debug print

    # cluster randomized macs to have unique identifiers
    log_result = []
    counter = 0
    for _, hash_group in disconnected_devices_hash_dict.items():
        result_matrix = analyze(hash_group, threshold) # list[list[dict]]
        # result matrix is a list of clusters [people]
        # each cluster is a list of packets that are supposed to be the same person
        for packet_cluster_list in result_matrix:
            for packet in packet_cluster_list:
                packet[ID] = counter
                log_result.append(packet)
            counter+=1

    # TODO: maybe add data packets that are sent from user devices [not AP]

    connected_mac_to_id = {} # each connected mac address gets an ID number
    # append all connected devices to dict
    for packet in connected_devices_packets:
        if packet[SRC_MAC] not in connected_mac_to_id:
            connected_mac_to_id[packet[SRC_MAC]] = counter
            counter+=1
        packet[ID] = connected_mac_to_id[packet[SRC_MAC]] # the new ID
        log_result.append(packet)
    
    # remove not needed fields
    if REMOVE_UNNEEDED_FIELDS_FROM_LOG_AFTER_CLUSTERING:
        for packet_dict in log_result:
            for key in list(packet_dict.keys()):
                if key not in [TIME, METERS, DBM, UNIT_ID, ID]:
                    packet_dict.pop(key)
    return sorted(log_result, key=lambda x: x[ID])
    
########### END USECASE FUNCTIONS ###########
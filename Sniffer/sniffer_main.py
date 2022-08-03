# common libs
from genericpath import isdir, isfile
from multiprocessing import Process
from os import kill, listdir, mkdir, remove
from datetime import datetime, timedelta
from signal import SIGTERM
from sys import argv
from time import sleep
import subprocess as sp
import json
import shutil
import atexit
import hashlib

# installed by default on kali linux
from scapy.layers.dot11 import Dot11ProbeReq, Dot11ProbeResp, RadioTap, Dot11, Dot11FCS, Dot11Beacon, Dot11EltRates, Dot11EltHTCapabilities, Dot11EltVendorSpecific
from scapy.all import *

# project modules
from firestore_api import get_sniffer_mode, upload_log_to_server
from preprocessing import BEACON, DATA, DBM, DST_MAC, ENABLED, FREQ, HASH, METERS, PROBE, SEQ, SRC_MAC, TIME, TYPE, UNIT_ID, dbm_2_meters
from sniffer_aux import add_index_to_screen_log, blocking_ping, calib_time, get_current_time, invoke_reset, is_tp_link, print_dbg, set_headless, start_monitor_mode, stop_monitor_mode, read_id, update_error_message, update_window_stamps
from sniffer_aux import log_folder,screen_logs_folder, not_uploaded_folder, uploaded_folder, raw_dump_folder, packets_log_file, screen_log_file, temp_pcapng, workdir
from sniffer_watchdog import start_watchdog

# GLOBALS
token = {}
unit_id = ""
watchdog_pid = 0
window_start_stamp: datetime
window_end_stamp: datetime
ap_addresses = set()
connected_addresses = set()
interface = "wlan0"
WATCHDOG_ON = False
# END GLOBALS

def exit_flow():
    global WATCHDOG_ON, interface
    if WATCHDOG_ON:
        kill(watchdog_pid, SIGTERM)
    stop_monitor_mode(interface)

def pre_init():
    for folder in [log_folder, screen_logs_folder, not_uploaded_folder, uploaded_folder, raw_dump_folder]:
        if not isdir(folder):
            mkdir(folder)
    with open(packets_log_file,"w"):
        pass # clear the file but keep it's existance
    if isfile(screen_log_file):
        add_index_to_screen_log()

def init_flow() -> bool:
    """
    @ everything related to init flow
    @ returns True if sniffer is active on config
    """
    global unit_id, token, watchdog_pid
    print_dbg("starting sniffer boot sequence\n")
    unit_id = read_id()
    with open(workdir + "/ServiceAccountKey.json", "r") as token_file:
        token = json.load(token_file)
    try:
        blocking_ping()
        calib_time()
        update_error_message(token, unit_id)
        mode = get_sniffer_mode(token, unit_id)
    except Exception as e:
        invoke_reset("failed on boot sequence: " + str(e))
    if mode == ENABLED:
        atexit.register(exit_flow)
        print_dbg("finished set up!\nsniffer id: " + str(unit_id) + "\n")
        if WATCHDOG_ON:
            watchdog_pid = start_watchdog()
        return True
    else:
        print_dbg("sniffer ID is disabled on config - exiting\n")
        return False

def get_next_stop(end_stamp) -> float:
    """
    should return number of seconds left for current time window
    """
    seconds = (end_stamp - get_current_time()) / timedelta(seconds=1)
    return seconds

def start_wireshark(interface, seconds):
	"""
	@ use TShark CLI to run wireshark for a given time
	@ interface would be wlan0mon
	"""
	if isfile(temp_pcapng):
		remove(temp_pcapng)
	assert seconds > 0 #TODO: change assert logic
	filter = "type data or type mgt subtype beacon or type mgt subtype probe-req"
	cmd = ["sudo", "tshark", "-i", interface, "-f", filter, "-w", temp_pcapng, "-a", "duration:" + str(seconds)]
	with open(screen_log_file, "a") as fp: # this file will be for watchdog and not for packets!!!
		sp.run(cmd, stdout=fp)

def dump_first_layer(packet: Packet) -> dict:
    """returns a dict of the first layer in the provided packet"""
    first = packet.copy()
    first.getlayer(0, _subclass=True).remove_payload()
    return first.fields

def digest_sha256(item: Any) -> str:
    """
    @ returns a sha256 of the string represntation of the input
    @ the input should have __str__ method
    """
    return hashlib.sha256(str(item).encode()).hexdigest()

def get_packet_hash(packet: Packet) -> str:
    """
    @ returns a a digested SHA256 signature based on Dot11EltRates, Dot11EltHTCapabilities packet layers
    @ this layers are considered hard to modify and should stay consistent for the same device between all probe request packets
    @ note that these layers are optional and some devices won't send these layers
    @ if any field was found to be inconsistent, it should be added to problematic_fields array
    """
    problematic_fields = ["SM_Power_Save"] # specific fields in the hard to modify layers that were found to be inconsistent
    hash_dict = {}
    current = ""
    current_layer = packet
    layers_dict = {"Dot11EltRates" : 0, "Dot11EltHTCapabilities" : 0} # hard to modify layers that we are testing
    while current_layer is not None:
        layer_name = str(current_layer.__class__)
        layer_name = layer_name[layer_name.find("scapy.layers.dot11.") + len("scapy.layers.dot11.") : layer_name.rfind("'")]
        if layer_name in layers_dict:
            layers_dict[layer_name] += 1
            current = layer_name + "_" + str(layers_dict[layer_name])
            tmp_dict = dump_first_layer(current_layer)
            for key, value in tmp_dict.items():
                if key in problematic_fields:
                    hash_dict[current + "_" + key] = "0"
                else:
                    hash_dict[current + "_" + key] = str(value)
        current_layer = current_layer.getlayer(1, _subclass=True) # get next layer
    return digest_sha256(hash_dict)

def convert_epoch_to_datetime_string(epoch: float) -> str:
    if not is_tp_link():
        epoch /= 1000
    return str(datetime.fromtimestamp(epoch))

def process_packet(caught_packet: Packet):
    """
    this function extracts the data needed and sends to server
    """
    global ap_addresses, connected_addresses
    current_time = get_current_time()
    if isfile(packets_log_file):
        openMode = 'a'
    else:
        openMode = 'w'
    packet_dict = {}
    should_save_packet = True
    packet_dict[TIME] = convert_epoch_to_datetime_string(float(caught_packet.time))
    packet_dict[UNIT_ID] = unit_id
    if caught_packet.haslayer(Dot11):
        packet_dict[DBM] = str(caught_packet[RadioTap].dBm_AntSignal)
        packet_dict[FREQ] = str(caught_packet[RadioTap].ChannelFrequency)
        packet_dict[METERS] = dbm_2_meters(packet_dict[DBM],packet_dict[FREQ])
        packet_dict[DST_MAC] = str(caught_packet[Dot11].addr1)
        packet_dict[SRC_MAC] = str(caught_packet[Dot11].addr2)
        packet_dict[SEQ] = str(caught_packet[Dot11FCS].SC)
        if caught_packet.haslayer(Dot11ProbeReq) and not caught_packet.haslayer(Dot11ProbeResp):
            packet_dict[TYPE] = PROBE
            packet_dict[HASH] = get_packet_hash(caught_packet)
        elif caught_packet.haslayer(Dot11Beacon) and packet_dict[SRC_MAC] not in ap_addresses:
            ap_addresses.add(packet_dict[SRC_MAC])
            packet_dict[TYPE] = BEACON
        elif caught_packet[Dot11].type == 2 and (packet_dict[SRC_MAC] not in connected_addresses or packet_dict[DST_MAC] not in connected_addresses): # data packet
            connected_addresses.add(packet_dict[SRC_MAC])
            connected_addresses.add(packet_dict[DST_MAC])
            packet_dict[TYPE] = DATA
        else: # ap/connected addresses already recorded, no need to record again
            should_save_packet = False
    else: # should not happen but just to be safe...
        should_save_packet = False
    if should_save_packet:
        #print_dbg(str(packet_dict) + "\n")
        with open(packets_log_file, openMode) as fp:
            fp.write(json.dumps(packet_dict) + '\n')
    else:
        #pet_watchdog() # so watchdog knows process is not dead
        pass

def process_packets(file_path: str) -> str:
    """
    should process the pcapng file to make a log to upload to db
    """
    global window_start_stamp, window_end_stamp, ap_addresses, connected_addresses
    time_window_string = window_start_stamp.isoformat(sep="_",timespec="seconds") + "_" + window_end_stamp.isoformat(sep="_", timespec="seconds")
    raw_dump_filename = raw_dump_folder + "/" + time_window_string + ".pcapng"
    shutil.move(temp_pcapng, raw_dump_filename)
    sniff(offline=raw_dump_filename, store=0, prn=lambda caught_packet: process_packet(caught_packet))
    ap_addresses = set() # clear temporary addresses after finishing current log
    connected_addresses = set()
    extracted_log_file = time_window_string
    if isfile(packets_log_file):
        shutil.move(packets_log_file, not_uploaded_folder + "/" + extracted_log_file)

def upload_data():
    """
    should upload any files in the not uploaded folder
    """
    global token
    logs_to_upload = listdir(not_uploaded_folder)
    for log in logs_to_upload: #file name is example: 24-05-22_10:50_24-05-22_11:00
        with open(not_uploaded_folder + "/" + log, "r") as log_file:
            data_to_upload = log_file.readlines()
        time_elements = log.split("_")
        date = time_elements[0]
        start = time_elements[1]
        stop = time_elements[3]
        start_stamp = datetime.fromisoformat(date + " " + start)
        stop_stamp = datetime.fromisoformat(date + " " + stop)
        try:
            if upload_log_to_server(token, data_to_upload, start_stamp, stop_stamp):
                shutil.move(not_uploaded_folder + "/" + log, uploaded_folder + "/" + log)
                print_dbg("uploaded log: " + log)
        except Exception as e:
            print_dbg("file name: " + log + " failed to upload to server\n")
            print_dbg("reason: " + str(e))

def main():
    if init_flow():
        while True:
            global window_start_stamp, window_end_stamp, token, unit_id, interface
            window_start_stamp, window_end_stamp = update_window_stamps(token, unit_id)
            interface = start_monitor_mode()
            seconds_to_run = get_next_stop(window_end_stamp)
            start_wireshark(interface, seconds_to_run) # will it be a blocking call?
            assert isfile(temp_pcapng) == True # TODO: change logic to not use assert, what happens if there is no file, or empty file
            tasks: list[Process] = []
            tasks.append(Process(target=stop_monitor_mode, args=(interface, True, )))
            tasks.append(Process(target=process_packets, args=(temp_pcapng,)))
            for task in tasks:
                task.start()
            for task in tasks:
                task.join()
            upload_data()
            
def countdown_start():
    set_headless()
    for i in range(10):
        print_dbg("sniffer will start automatically in " + str(10-i) + " seconds\nrun ./stop_sniffer.sh to stop it\n")
        sleep(1)

if __name__ == "__main__":
    pre_init()
    if len(argv) > 1 and argv[1] == "headless":
        countdown_start()
    main()

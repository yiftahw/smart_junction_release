from typing import Tuple
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime, timedelta
import timeit
import json
from preprocessing import merge_logs

### GLOBALS ###
CONFIG = "config"
THRESHOLDS = "thresholds"
DATA = "data"
WINDOW_SIZE = "timeframe_minutes"
is_app_initialized = False
### GLOBALS ###

"""
TODO:
finish logic to download from more than one timestamp
add logic to delete collections
"""
# @@@@@ AUX FUNCTIONS @@@@@
def get_ids_from_document(document) -> list[str]:
    ids_list = []
    for collection in document:
        ids_list.append(collection.id)
    return ids_list

def init_firebase(account_token: dict):
    cred = credentials.Certificate(account_token)
    global is_app_initialized
    if not is_app_initialized:
        firebase_admin.initialize_app(cred)
        is_app_initialized = True
    return firestore.client()

# @@@@@ END AUX FUNCTIONS @@@@@


def get_config_data(account_token: dict) -> dict:
    """
    might return an empty dict if config was not found on server!
    """
    db = init_firebase(account_token)
    config_data = db.collection(CONFIG).document(CONFIG).get() # get dict from document     
    return config_data.to_dict()

def get_thresholds_data(account_token: dict) -> dict:
    """
    might return an empty dict if config was not found on server!
    """
    db = init_firebase(account_token)
    config_data = db.collection(THRESHOLDS).document(THRESHOLDS).get() # get dict from document     
    return config_data.to_dict()


def get_window_timestamps(account_token: dict, current_time: datetime) -> Tuple[datetime, datetime]:
    """
    returns the timestamps of the current timeframe
    this function should pull the config file from the server before starting to log information
    together with the current time, will calculate when the time window closes to start uploading.
    [we need to assume the config time window length divides 60 minutes with no remainder]
    example:
    current time is 17:32
    time window on server is 10 minutes
        ->  current time window is 17:30 to 17:40
            logging will stop on 17:40
            log timestamp will be 17:30_17:40 even though logging started on 17:32
            this is to simplify synchronization of data
    """
    config_dict = get_config_data(account_token)
    window_length = int(config_dict[WINDOW_SIZE])
    window_end = datetime(current_time.year,current_time.month,current_time.day,current_time.hour, 0)
    delta = timedelta(minutes=window_length)
    while True:
        window_end+=delta
        if window_end > current_time:
            return window_end - delta, window_end

    
def get_sniffer_mode(account_token: dict, unit_id: int) -> str:
    config_data = get_config_data(account_token)
    unit_id_key = "unit" + str(unit_id)
    return config_data[unit_id_key]


def get_dates(account_token: dict) -> list[str]:
    """
    """
    db = init_firebase(account_token)
    data_collection = db.collection(DATA).get()
    dates_list = get_ids_from_document(data_collection)
    return dates_list


def get_times_from_date(account_token: dict, date: str) -> list[str]:
    db = init_firebase(account_token)
    times_collections = db.collection(DATA).document(date).collections() # get sub-collections from document
    times_list = get_ids_from_document(times_collections)
    return times_list


def get_data_from_date_timestamp(account_token: dict, date: str, timestamp: str) -> list[dict]:
    """
    @ TODO: add logic to pull more than 1 timestamp?
    """
    db = init_firebase(account_token)
    logs_documents = db.collection(DATA).document(date).collection(timestamp).stream()
    logs_dict = {}
    redundancy_map = {}
    for log_doc in logs_documents:
        if log_doc.id.find("unit") != -1:
            logs_dict[log_doc.id] = log_doc.to_dict()[DATA]
        if log_doc.id.find("redundancy_map") != -1:
            redundancy_map = log_doc.to_dict()
    if len(logs_dict) > 1:
        return merge_logs(logs_dict, redundancy_map)
    elif len(logs_dict) == 1:
        return logs_dict[list(logs_dict.keys())[0]]
    else:
        return []


def get_data_from_datetime(account_token: dict, date: str, start_time: str, end_time: str) -> dict:
    """
    not implemented yet!
    """
    """
    db = init_firebase(account_token)
    start_time = time.fromisoformat(start_time)
    end_time = time.fromisoformat(end_time)
    times_list = get_times_from_date(account_token, date)
    times_window = []
    for item in times_list:
        temp_item_start = time.fromisoformat(item.split("_")[0])
        temp_item_end   = time.fromisoformat(item.split("_")[1])
        if temp_item_start >= start_time and temp_item_end <= end_time:
            times_window.append(item)
    print(times_window)
    """
    print("not implemented yet!")
    return {}

def upload_config_to_server(account_token: dict, config: dict, merge_configs: bool = False) -> bool:
    """
    @ account_token - a dict containing the token from firestore
    @ config - a dict containing any parameters needed for the sniffers
    @ merge_configs - boolean indicating if configs should be merged or overriden completely
    @ if false, the function will override any existing config params!
    """
    db = init_firebase(account_token)
    db.collection(CONFIG).document(CONFIG).set(config, merge_configs)
    result = get_config_data(account_token)
    return config.items() <= result.items()

def upload_thresholds_to_server(account_token: dict, thresholds: dict, merge_configs: bool = False) -> bool:
    db = init_firebase(account_token)
    db.collection(THRESHOLDS).document(THRESHOLDS).set(thresholds, merge_configs)
    result = get_thresholds_data(account_token)
    return thresholds.items() <= result.items()

def upload_log_to_server(account_token: dict, data: list[str], window_start_stamp: datetime, window_end_stamp: datetime) -> bool:
    """
    """
    if len(data) == 0:
        return False
    start = timeit.default_timer()
    db = init_firebase(account_token)
    data_to_upload = []
    for packet in data:
        data_to_upload.append(json.loads(packet))
    data_dict = {"data" : data_to_upload}
    start_time = window_start_stamp.strftime("%H:%M")
    end_time = window_end_stamp.strftime("%H:%M")
    packets_date = datetime.fromisoformat(data_to_upload[0]["time"]).date().isoformat()
    unit_id = data_to_upload[0]["unit_id"]
    db.collection(DATA).document(packets_date).set({"what is the answer?" : "42"})
    db.collection(DATA).document(packets_date).collection(start_time + "_" + end_time).document("unit" + str(unit_id)).set(data_dict)
    stop = timeit.default_timer()
    print('**************************\n****SUCCESS UPLOAD*****\n**************************')
    print("Time taken " + str(stop - start))
    return True


def end_unit_handshake(account_token: dict, unit_id: str, time_stamp: datetime, error_reason: str = ""):
    temp_dict = {}
    time_stamp = datetime(time_stamp.year,time_stamp.month,time_stamp.day,time_stamp.hour,time_stamp.minute,time_stamp.second,0)
    temp_dict["unit" + unit_id + "_timestamp"] = time_stamp.isoformat(sep=" ")
    if len(error_reason) != 0:
        temp_dict["unit" + unit_id + "_error"] = error_reason
    return upload_config_to_server(account_token,temp_dict, True)


def delete_data(account_token: dict, date: str, start_time: str, end_time: str) -> bool:
    """
    """
    print("not implemented")
    return False   


if __name__ == "__main__":
    pass
from genericpath import isfile
from os import listdir, remove, system
from shutil import copy, SameFileError, move
import shutil
from time import sleep
import ntplib
from datetime import datetime
from netifaces import interfaces
import subprocess
from firestore_api import end_unit_handshake, get_window_timestamps


headless = False
workdir = "/root/Desktop/smart_junction-master"
packets_log_file = workdir + '/data_log'
temp_pcapng = workdir + "/tmp_data.pcapng"

log_folder          = "/root/Desktop/logs"
not_uploaded_folder = log_folder + "/not_uploaded"
uploaded_folder     = log_folder + "/uploaded"
screen_logs_folder  = log_folder + "/screen_logs"
raw_dump_folder     = log_folder + "/raw_dump"

screen_log_file     = log_folder + "/screen_log"
error_log           = log_folder + "/error_log"
latest_error        = log_folder + "/latest_error"

tplink_found = False

##### FUNCTIONS #####

def set_headless():
	global headless
	headless = True


def add_index_to_screen_log():
    global log_folder
    files = listdir(screen_logs_folder)
    max_index = 0
    for filename in files:
        if filename.find("screen_log") != -1:
            index = filename[len("screen_log"):]
            if len(index) > 0 and int(index) > max_index:
                max_index = int(index)
    move(screen_log_file, screen_logs_folder + "/screen_log" + str(max_index + 1))
    

def print_dbg(msg: str, clean: bool = False):
    global headless, screen_log_file
    if headless == False:
        print(msg)
    else:
        log_exists = isfile(screen_log_file)
        if clean and log_exists:
            add_index_to_screen_log()
            log_exists = False
        else:
            if log_exists:
                open_mode = "a"
            else:
                open_mode = "w"
            with open(screen_log_file, open_mode) as out:
                out.write(msg)


def log_error(reason: str, stamp: datetime) -> None:
    stamp = datetime(stamp.year,stamp.month,stamp.day,stamp.hour,stamp.minute,stamp.second,0)
    stamp = stamp.isoformat(sep=" ")
    error_message = "time: " + stamp + "\t\treason: " + reason + "\n"
    if isfile(error_log):
        open_mode = "a"
    else:
        open_mode = "w"
    print_dbg(reason)
    with open(error_log, open_mode) as error_file:
        error_file.write(error_message)
    with open(latest_error, "w") as latest_error_file:
        latest_error_file.write(error_message)


def invoke_reset(reason: str) -> None:
    global packets_log_file, log_folder
    stamp = datetime.now()
    log_error(reason,stamp)
    if reason == "watchdog failed":
        shutil.copy(packets_log_file, log_folder + "/failed_window_" + stamp.isoformat(sep="_",timespec="seconds"))
    system("sudo shutdown -r now")


def blocking_ping():
    """
    loop until internet connection is availible
    """
    sleep_time = 1
    stuck_threshold = 60 # seconds threshold to assume raspberry is stuck
    sleep_time_count = 0
    while True:
        sleep(sleep_time)
        resp = system("ping -c 2 www.google.com") # -c limits the ping to two packets
        if resp == 0:
            print_dbg("ping success\n")
            return
        else:
            print_dbg("ping failed\n")
            sleep_time_count+=sleep_time
            if sleep_time_count > stuck_threshold:
                invoke_reset("ping failed")


def calib_time():
    while True:
        try:
            call = ntplib.NTPClient()
            response = call.request('il.pool.ntp.org', version=3)
            temp = datetime.fromtimestamp(response.tx_time).timestamp()  # timestamp() converts ntp's answer into epoch
            print_dbg("ntp sync success\n")
            return temp
        except ntplib.NTPException:
            print_dbg("ntp failed, sending another request\n")


def is_tp_link():
    global tplink_found
    return tplink_found

def calib_timezone():
	system("sudo timedatectl set-timezone Asia/Jerusalem")

def start_monitor_mode() -> str:
    """
    @ searches for an interface to start in monitor mode, and activates it
    @ returns the name of the interface chosen to be in monitor mode
    """
    interface = "wlan0"
    output = subprocess.check_output("sudo airmon-ng", shell=True).decode("utf-8")
    global tplink_found
    for line in output.split("\n"):
        if len(line) > 0 and line.find("Chipset") == -1 and line.find("TP-Link") != -1:
            interface = line[line.index("wlan") : line.index("wlan") + len("wlan0")]
            tplink_found = True
    system("sudo airmon-ng check kill")
    system("sudo airmon-ng start " + interface)
    if tplink_found == False:
        interface += "mon"
    return interface # when airmon starts monitor mode, a new interface is created: wlan0 disabled, wlan0mon activated

def stop_monitor_mode(interface: str, blocking: bool = False):
    ifaces_list = interfaces()
    if interface in ifaces_list:
        system("sudo airmon-ng stop " + interface)
        system("sudo systemctl start NetworkManager")
        try: # sometimes entering monitor mode deletes the system's DNS config file 
            copy("/root/Desktop/smart_junction-master/install_headless/resolv.conf", "/etc/resolv.conf")
        except SameFileError:
            pass
    if blocking:
        blocking_ping()

def get_current_time() -> datetime:
    return datetime.now()    

def update_error_message(token: dict, station_id: str):
    latest_error_message = ""
    current_time = get_current_time()
    if isfile(latest_error):
        with open(latest_error, "r") as log_file:
            latest_error_message = log_file.readline()
        remove(latest_error)
        end_unit_handshake(token, station_id , current_time, latest_error_message)

def update_window_stamps(token: dict, unit_id: str):
    current_time = get_current_time()
    end_unit_handshake(token, unit_id, current_time)
    return get_window_timestamps(token, current_time)

def show_ifaces():
    system("ifconfig")

def read_id():
    idp = open('/root/Desktop/ID', 'r')
    temp = idp.read().strip()
    idp.close()
    return temp
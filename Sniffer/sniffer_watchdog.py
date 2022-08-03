from genericpath import isfile
from os import system, fork
from os.path import getmtime
from sniffer_aux import packets_log_file, invoke_reset
from time import sleep

sleep_threshold = 120 # seconds

def watchdog():
    """
    if data log file was not updated for more than 2 minutes, restart the device
    """
    sleep(sleep_threshold) # let init flow run until starting to sniff, maybe takes around 30 seconds
    while True:
        if isfile(packets_log_file):
            current_timestamp = getmtime(packets_log_file)
            sleep(sleep_threshold)
            previous_timestamp = current_timestamp
            current_timestamp = getmtime(packets_log_file)
            if current_timestamp == previous_timestamp: # file was not edited for 120 seconds, assume sniffer is stuck
                system("sudo systemctl status rc-local.service > /root/Desktop/status_before_watchdog_restart") # save rc-local status
                invoke_reset("watchdog failed")


def start_watchdog() -> int:
    """
    @ fork a new process, and start watch dog in the new process
    @ if data log file was not updated for more than 2 minutes, restart the device
    @ returns watchdog's pid
    """
    pid = fork()
    if pid > 0:
        return pid # this is sniffer's original process, return
    if pid == 0:
        watchdog() # this is the new watchdog process


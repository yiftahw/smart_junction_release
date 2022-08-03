from os import getcwd, system
from shutil import move
from time import sleep

def generate_rc_local(path):
    #generate the boot service file to automatically open a bash window and run the sniffer in it.
    with open("install_headless/rc.local","w") as rclocal_file:
        lines = []
        lines.append("#!/bin/sh -e\n")
        lines.append("sleep 10\n")
        lines.append("sudo python " + path + "/sniffer_main.py headless\n")
        lines.append("exit 0\n")
        rclocal_file.writelines(lines)

def install_dependencies():
    system("yes | sudo apt update")
    system("yes | sudo apt install pip")
    system("yes | pip install ntplib")
    system("yes | pip install firebase_admin")
    system("yes | pip install firebase")
    system("yes | pip install netifaces")

def install_headless():
    print("make sure you run this script in sudo mode!")
    print("otherwise it might not work properly!")

    sleep(5)

    id = input("please enter unit-id: ")
    with open('/root/Desktop/ID', 'w') as file_stream:
        file_stream.write(id)

    install_dependencies()

    project_folder = getcwd()
    headless_folder = project_folder + "/install_headless"
    generate_rc_local(project_folder)

    #move the files to their destination
    move(headless_folder + "/rc.local", "/etc/rc.local")
    move(headless_folder + "/rc-local.service", "/etc/systemd/system/rc-local.service")

    #commands to enable rc.local service
    system("sudo chmod 777 /etc/rc.local")
    system("sudo chmod 777 " + project_folder + "/stop_sniffer.sh")
    system("sudo chmod 777 " + project_folder + "/stream_sniffer_to_screen.sh")
    system("sudo sudo systemctl enable rc-local")
    system("sudo timedatectl set-timezone Asia/Jerusalem")  

if __name__ == "__main__":
    install_headless()
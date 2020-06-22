#pip3 install requests
#cron-tab: */2 * * * * sudo python3 home/pi/Desktop/script.py

import os

import requests
from datetime import datetime

URL = "https://www.loven4ever.com/admin"
COMMAND_ON_ERROR = "sudo service apache2 restart"

def log(message: str):
    with open("log.txt", "a") as myfile:
        myfile.write(datetime.now().__str__() + message + "\n")
        os.system(COMMAND_ON_ERROR)

def main():
    try:
        r = requests.get(URL)
        print("Website working, doing nothing")
        log("Alright")
    except requests.exceptions.ConnectionError:
        print("Website down, rebooting Apache2")
        log("Fixed")
        os.system(COMMAND_ON_ERROR)

if __name__ == "__main__":
    main()
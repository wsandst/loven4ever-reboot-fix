#pip3 install requests

import os

import requests
from datetime import datetime

URL = 'https://loven4ever.com/admin'
ERROR_STATUS_CODE = 204
COMMAND_ON_ERROR = "sudo service apache2 restart"

def main():
    r = requests.get(URL)
    print(r.status_code)
    if (r.status_code == ERROR_STATUS_CODE):
        with open("log.txt", "a") as myfile:
            myfile.write(datetime.now().__str__() + " Fixed \n")
            os.system(COMMAND_ON_ERROR)

if __name__ == __name__:
    main()
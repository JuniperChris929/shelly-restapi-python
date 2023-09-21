import requests
import json
import urllib
import openpyxl
import logging
import getpass
from requests.auth import HTTPBasicAuth


username_arg = input("Please enter the username: ")
password_arg = getpass.getpass()


try:
    readbook = openpyxl.load_workbook("iplist.xlsx")
    sheet_shelly = readbook["shelly"]
    #rows_shelly = sheet_shelly.rows
    rows_shelly = list(sheet_shelly)
    rowcount = sheet_shelly.max_row
    rowcounter = 1
except Exception as err:
    exit()


for row_active in range(1,rowcount):
    if rows_shelly[row_active][0].value != "":
        try:
            hostname_arg = str(rows_shelly[row_active][0].value)
            response = requests.get(
              'http://' + hostname_arg + '/status', 
              auth=HTTPBasicAuth(username_arg, password_arg)
            )
            data = response.json()
            print("IP: " + hostname_arg + ", Temperature: " + str(data['temperature']) + "°C")

        except Exception as err:
            logging.info('Error detected for ' + str(rows_shelly[row_active][0].value))
            print("IP: " + hostname_arg + ", Temperature: Error getting value from Device")
            continue

        finally:
            logging.info('Script has ended!')
            print("\n")

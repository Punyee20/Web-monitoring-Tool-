import urllib3
import requests
import datetime
from datetime import datetime
import time
import logging
import sys
import os
import logging
from stat import S_IREAD, S_IRGRP, S_IROTH
import shutil
from urllib.request import urlopen

requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
try:
    requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
except AttributeError:
    pass

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
print(datetime.now())
filename=datetime.now().strftime("USlog_%d-%m-%Y_%H.%M.log")


print("CII List started.")
websitesList = ["http://localhost/"
]


def check(url):
    try:
        req = requests.get(url, headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/96.0.4664.45 Safari/537.36"}, verify=False)
        status_code = req.status_code
        print(status_code)

        if 100 <= status_code <= 199:
            print("Informational response received.")
        elif 200 <= status_code <= 299:
            print("Website is up ")

        elif 300 <= status_code <= 399:
            print("website is redirected")
            time.sleep(8)
            req = requests.get(url)
            status_code1 = req.status_code
            print(status_code)
            msg = "CII::Website is redirected! Check the URL: {urll} status code: {stcode}".format(urll=url,
                                                                                                  stcode=status_code1)

            print(msg)
            baseurl = 'https://api.telegram.org/bot5864172746:AAFMq6PZ8cTCOuOtKiiGGczOdkj6bazC8XU/sendMessage?chat_id=-883542168&text=' + msg
            requests.get(baseurl)
            if 300 <= status_code1 <= 399:
                print("website redirected!")
            elif 400 <= status_code1 <= 599:
                print("Client side error or server side error! Please check!")

            elif 200 <= status_code1 <= 299:
                print("No error")

        elif 400 <= status_code <= 499:
            print("Client side error")
            time.sleep(8)
            req = requests.get(url)
            status_code2 = req.status_code
            print(status_code)
            msg = "Client side error! Check the URL: {urll} status code: {stcode}".format(urll=url,
                                                                                              stcode=status_code2)

            print(msg)
            baseurl = 'https://api.telegram.org/bot5864172746:AAFMq6PZ8cTCOuOtKiiGGczOdkj6bazC8XU/sendMessage?chat_id=-883542168&text=' + msg
            requests.get(baseurl)

            if 400 <= status_code2 <= 499:
                print("Client side error!")
            elif 500 <= status_code2 <= 599:
                print("Server side error! Please check!")
            elif 200 <= status_code2 <= 299:
                print("No error")

        elif 500 <= status_code <= 599:
            time.sleep(8)
            print("server side error")
            req = requests.get(url)
            status_code3 = req.status_code
            print(status_code)
            msg = "SLT::Server side error! Check the URL: {urll} status code: {stcode}".format(urll=url,
                                                                                              stcode=status_code)
            print(msg)
            baseurl = 'https://api.telegram.org/bot5864172746:AAFMq6PZ8cTCOuOtKiiGGczOdkj6bazC8XU/sendMessage?chat_id=-883542168&text=' + msg

            requests.get(baseurl)

            if 300 <= status_code3 <= 399:
                print("website redirected!")
            elif 500 <= status_code3 <= 599:
                print("Server side error! Please check!")
            elif 200 <= status_code3 <= 299:
                print("No error")

    except requests.Timeout as err:
        print("Timeout error in website")
        msg = "Timeout error in website {urll}".format(urll=url)

        print(msg)
        baseurl = 'https://api.telegram.org/bot5864172746:AAFMq6PZ8cTCOuOtKiiGGczOdkj6bazC8XU/sendMessage?chat_id=-883542168&text=' + msg
        requests.get(baseurl)
        pass


length = len(websitesList)
print(length)

for x in range(length):
    try:
        print(websitesList[x])
        check(websitesList[x])
    except Exception as error:
        msg1 = "Exception occured! please check! " +websitesList[x] +" "+str(error)

        print(msg1+"\n")
        baseurl = 'https://api.telegram.org/bot5864172746:AAFMq6PZ8cTCOuOtKiiGGczOdkj6bazC8XU/sendMessage?chat_id=-883542168&text=' + msg1
        requests.get(baseurl)
        continue






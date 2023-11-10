import requests
import urllib3
import credentials
import time
import datetime

BOT_TOKEN = credentials.BOT_TOKEN
GROUP_CHAT_ID = credentials.GROUP_CHAT_ID
SERVER_DOWN = False

x = datetime.datetime.now()
time_now = x.strftime("%d" " %b")


def checkserver():
    global SERVER_DOWN
    # Checks to see if you have an internet connection
    url = 'https://www.lugetech.com/'
    try:
        print('Checking server status')
        response = urllib3.request("GET", url)
        response.close()
        if SERVER_DOWN:
            SERVER_DOWN = False
            message = "Alert! Your server is back up on " + time_now
            requests.get(
                'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage?chat_id=' + GROUP_CHAT_ID + '&text=' + message)
    except Exception as e:
        if not SERVER_DOWN:
            SERVER_DOWN = True
            message = "Alert! Your server is down on " + time_now
            requests.get(
                'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage?chat_id=' + GROUP_CHAT_ID + '&text=' + message)


while True:
    checkserver()
    time.sleep(3600)
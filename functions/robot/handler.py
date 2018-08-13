import json
import requests
import urllib3
import sys
import os

urllib3.disable_warnings()

def check_TF():
    data = open(os.path.join(sys.path[0], "test.text"), "r")
    if "| PASS |" in data.read():
        return 'Running Robot Framework. The device has passed all required tests'
    else:
        return 'Running Robot Framework. The device has failed a test'

def handle():
    try:
        webhook_url = os.environ['token']
        slack_data = {'text': check_TF() }
        response = requests.post(
            webhook_url, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'})
        print response
    except:
        print("Check Slack for issues")

handle()

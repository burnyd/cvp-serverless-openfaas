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
        webhook_url = 'https://hooks.slack.com/services/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'
        slack_data = {'text': check_TF() }
        response = requests.post(
            webhook_url, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'})
        print response
    except:
        print("Check Slack for issues")

handle()

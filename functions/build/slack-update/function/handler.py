import json
import requests
import urllib3
import os

urllib3.disable_warnings()

def handle(req):
    try:
        webhook_url = os.environ['token']
        slack_data = {'text': "Device '%s' now being added" % req}
        response = requests.post(
            webhook_url, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'})
        print response
    except:
        print("Check Slack for issues")

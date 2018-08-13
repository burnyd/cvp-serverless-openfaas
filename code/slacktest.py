import json
import requests
import urllib3
import os

urllib3.disable_warnings()

def handle(req):
    try:
        webhook_url = 'https://hooks.slack.com/services/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'
        slack_data = {'text': "Device '%s' now being added" % req}
        response = requests.post(
            webhook_url, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'})
        print response
    except:
        print("Check Slack for issues")

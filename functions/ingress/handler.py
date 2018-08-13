import json
import requests
import urllib3

urllib3.disable_warnings()
url = 'http://10.20.30.147:31112/function/slack-update'
roboturl = 'http://10.20.30.147:31112/function/robot'

def handle(req):
    #slack_update(req)
    r = requests.post(url, data=req)
    robot = requests.post(roboturl, data=req)

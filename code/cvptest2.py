#Openfaas magic.
#I need to get the entire JSON data with the device because things may need it!  This includes also a new way to send the post request header.
#Dockerize this thing with arguments for container, IP, Username and password.

from cvprac.cvp_client import CvpClient
import json
import time
import urllib3
import requests

urllib3.disable_warnings()
client = CvpClient()
client.connect(['10.20.30.142'],'daniel', 'daniel123')
url = 'http://10.20.30.147:31112/function/hello-python'
data_list1 = []
data_list2 = []
data_device = {}

def get_devices(data_list):
    inventory = client.api.get_devices_in_container('DC1-Leaf')
    data = json.dumps(inventory, sort_keys=True, indent=4)
    data_dict = json.loads(data)
    for devices in data_dict:
        showdevices = devices['ipAddress']
        data_list.append(showdevices)
        showhosts = devices['fqdn']
        data_list.append(showdevices)
        data_device.update({showhosts:showdevices})

def main():
    while True:
        print "*********Checking for diff of devices*********"
        get_devices(data_list1)
        time.sleep(0.9)
        get_devices(data_list2)
        check_devices = list(set(data_list2) - set(data_list1))
        str_check_devices = ''.join(map(str, check_devices))
        if data_list1 != data_list2:
            host = [k for k,v in data_device.items() if v == str_check_devices]
            str_host = ''.join(map(str, host))
            hostip = {str_host:str_check_devices}
            hostip_json = json.dumps(hostip)
            print "changes found for device %s with the ip address of %s has been moved" % (str_host, str_check_devices)
            r = requests.post(url, data=str_check_devices)
            q = requests.post(url, data=hostip)
            s = requests.post(url, json=hostip_json)
            print(q.text)
            print(r.text)
            print(s.text)
            print(s.json)
            break
main()

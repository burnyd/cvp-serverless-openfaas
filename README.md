### Using Serverless / Openfaas to monitor Arista Cloud vision network devices.

This is a example of using Arista CVP and Openfaas as API gateway for serverless functions.  The idea here is that when a network event happens that we rely too much on manual intervention to find an issue within our network operations.  It would be nice to pivot that mentality and use serverless functions in a manor that would send an alert upon a trigger.  In this case a network device is added on to the network.  Normally, once a device is added to the network it has to be added to a CMDB or notified via a chatops way.  After a device is added typically a device has to be checked to see if it is considered healthy.  So it would be nice to have this automatically added and have unit tests to check to see if the device is the 'intent' of the operator so they do not have to log into the device.

![Alt text](1000ft.jpg?raw=tr1000ft.jpgue "1000ft view")

The idea here is that a device is moved into a container which is simply a grouping within cloud vision.  A container which runs on cloud vision monitors the CVP API for changes.  Once a change happens it will fire off a rest call into Openfaas API gateway as a serverless function.

![Alt text](openfaas-function-views.jpg?raw=true "Openfaas view")

That function will then notify slack that a device has moved.  It will then chain another function which will run robot framework against the device to see if it is the the intent of the operator.  


![Alt text](webhook.jpg?raw=true "Slack webhook")

## Requirements
- A Kubernetes cluster.  This was running 1.10
- OpenFaas. 
- Arista Cloud vision 2018.1.x 

From Arista cloud vision.
curl -fsSL get.docker.com -o get-docker.sh && ./get-docker.sh
service docker restart


docker pull burnyd/cvpserverless

docker run cvpserverless 10.20.30.142 daniel daniel123 DC1-Leaf 10.20.30.147 #Arguments inline cvpserver username password container openfaas api gateway 

Once that is installed simply clone this repo and install stack.yaml to deploy the containers to openfaas. 

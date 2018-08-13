*** Settings ***
Documentation     This is a test that will check to see if interfaces are in the up up state.
...               The test reverts the neighbor statement to it's proper state.
Suite Setup       Connect To Switches
Suite Teardown    Clear All Connections
Library           AristaLibrary
Library           AristaLibrary.Expect
Library           Collections
Library    network_validation.Bgp

*** Test Cases ***
show ip interfaces
   Record Output    cmd=show ip interface

*** Keywords ***
Connect To Switches
    [Documentation]    Establish connection to a switch which gets used by test cases.

    Connect To    host=${SW1_HOST}    transport=${TRANSPORT}    username=${USERNAME}    password=${PASSWORD}
    Get Command Output  cmd=show ip interface
    Expect  interfaces Ethernet1 interfaceStatus  to be  connected

Gather Post Change Output
    Record Output    cmd=show ip interfaces


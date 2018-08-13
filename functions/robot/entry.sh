#!/bin/sh

while read line
do
  echo "$line"
done < "${1:-/dev/stdin}"

#echo $line SW1_HOST  >> /etc/hosts validate_network.py --config interfaces.yaml > test.text && python slack.py
echo 10.20.30.157 SW1_HOST  >> /etc/hosts && validate_network.py --config interfaces.yaml > test.text && python slack.py

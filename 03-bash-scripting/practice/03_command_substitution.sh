#!/bin/bash

echo "Welcome $USER on $HOSTNAME"
echo "#################################"

FREERAM=$(free -m | grep Mem | awk '{print $4}')

LOAD=$(uptime | awk '{print $9}')

ROOTFREE=$(df -h | grep '/dev/sda1' | awk '{print $4}')

echo "##########################################"
echo "Available RAM is $FREERAM MB"
echo "Current Load is $LOAD"
echo "Root partition free space is $ROOTFREE"
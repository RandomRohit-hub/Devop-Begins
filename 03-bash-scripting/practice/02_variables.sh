#!/bin/bash

# this script prints system info

# variable declaration
PACKAGE="httpd wget unzip"
SVC="httpd"
URL="https://www.tooplate.com/zip-templates/2098_health.zip"
ART_NAME="2098_health"
TEMPDIR="/temp/webfiles"

echo "welcome to first script"
echo

echo "####################################"

echo "Packages to install are: $PACKAGE"

echo "Service name is: $SVC"

echo "Website URL is: $URL"

echo "Artifact name is: $ART_NAME"

echo "Temporary directory is: $TEMPDIR"

echo "####################################"

echo "The uptime of system is:"
uptime

echo "####################################"

echo "Memory utilization:"
free -m

echo "####################################"

echo "Disk utilization:"
df -h
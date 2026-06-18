#!/bin/bash

systemctl is-active --quiet httpd

if [ $? -eq 0 ]
then
        echo "httpd process is running"
else
        echo "httpd process is not running"
        echo "Starting httpd service..."

        systemctl start httpd

        if [ $? -eq 0 ]
        then
                echo "Process started successfully"
        else
                echo "Process starting failed"
        fi
fi
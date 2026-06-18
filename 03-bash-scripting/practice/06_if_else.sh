#!/bin/bash

read -p "Enter a number: " NUM
echo

if [ $NUM -gt 100 ]
then
    echo "We have entered the IF block"
    sleep 3
    echo "Your number is greater than 100"
    echo
    date
fi

echo "Script execution completed successfully"


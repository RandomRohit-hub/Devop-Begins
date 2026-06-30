#!/usr/bin/python3
# Module 10: OS Automation - Checking File/Directory Existence
import os

path = '/tmp/testfile.txt'

if os.path.isdir(path):
    print(f"'{path}' is a directory.")
elif os.path.isfile(path):
    print(f"'{path}' is a file.")
else:
    print(f"'{path}' does not exist.")

#!/usr/bin/python3
# Module 10: OS Automation - Managing System Users and Groups
# Demonstrates running shell commands and system tasks using the 'os' module.
import os

userlist = ["alpha", "beta", "gamma"]

print("Adding users to system...")
print("#" * 90)

# Loop to check and add users
for user in userlist:
    # os.system executes shell command and returns the exit status code (0 is success)
    exitcode = os.system(f"id {user} >/dev/null 2>&1")
    if exitcode != 0:
        print(f"User {user} does not exist. Adding it.")
        print("-" * 45)
        os.system(f"sudo useradd {user}")
    else:
        print(f"User {user} already exists, skipping.")
        print("-" * 45)

# Check if group 'science' exists, create if not
exitcode = os.system("grep -q science /etc/group")
if exitcode != 0:
    print("Group 'science' does not exist. Adding it.")
    print("-" * 45)
    os.system("sudo groupadd science")
else:
    print("Group 'science' already exists, skipping.")
    print("-" * 45)

# Add users to the 'science' group
for user in userlist:
    print(f"Adding user {user} to the 'science' group.")
    print("-" * 45)
    os.system(f"sudo usermod -G science {user}")

print("Creating directory /opt/science_dir...")
print("-" * 45)

# Using os.path.isdir to check directories
if os.path.isdir("/opt/science_dir"):
    print("Directory /opt/science_dir already exists, skipping.")
else:
    os.system("sudo mkdir -p /opt/science_dir")

print("Assigning permission and ownership...")
print("-" * 45)
os.system("sudo chown :science /opt/science_dir")
os.system("sudo chmod 770 /opt/science_dir")
print("OS Tasks Automation Completed.")

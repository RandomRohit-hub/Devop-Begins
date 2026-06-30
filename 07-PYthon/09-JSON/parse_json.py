#!/usr/bin/python3
# Module 9: JSON - Parsing JSON in Python
# DevOps scripts frequently parse JSON outputs from AWS CLI, Kubernetes API, or Ansible.
import json
import os

# Get path to the JSON file in the same directory
dir_path = os.path.dirname(os.path.realpath(__file__))
json_file_path = os.path.join(dir_path, "learn_json.json")

# 1. Load JSON file into a Python Dictionary
with open(json_file_path, "r") as file:
    data = json.load(file)

print("Parsed JSON data as a Python Dictionary:")
print(data)
print("-" * 30)

# 2. Access elements
print("DevOps Skills:", data["DevOps"])
print("Ansible Python Path:", data["ansible_facts"]["python"])
print("-" * 30)

# 3. Modify and serialize back to string
data["DevOps"].append("Terraform")
json_string = json.dumps(data, indent=2)
print("Modified data serialized back to JSON string:")
print(json_string)

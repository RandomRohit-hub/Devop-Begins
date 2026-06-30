#!/usr/bin/python3
# Module 6: Functions - Calling Modern Module (Method 2)
# Using 'from modern import *' imports functions directly into namespace.
import sys
import os

# Ensure the script directory is in the path to find the modern module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from modern import *

print("Importing everything directly from 'modern':")
order_food("Pizza")
vac_feedback(efficacy=34, vac="Unknown")
time_activity(10, 20, 10, hobby="Dance", sport="Boxing", fun="Driving", work="DevOps")

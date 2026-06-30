#!/usr/bin/python3
# Module 6: Functions - Calling Modern Module (Method 1)
# Using 'import modern' requires prefixing functions with the module name.
import sys
import os

# Ensure the script directory is in the path to find the modern module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import modern

print("Importing complete module 'modern':")
modern.order_food("Salad", "Pizza", "Biryani", "Soup")
modern.vac_feedback(efficacy=34, vac="Unknown")
modern.time_activity(10, 20, 10, hobby="Dance", sport="Boxing", fun="Driving", work="DevOps")

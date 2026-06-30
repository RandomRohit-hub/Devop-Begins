#!/usr/bin/python3
# Module 1: Python Basics - Variables
# Variables are containers for storing data values.

# 1. Variable Assignments with Data Types
var1 = "Python"   # String (str)
var2 = 75         # Integer (int)
var3 = 3.5        # Floating point number (float)

# Printing Variables
print("var1:", var1)
print("var2:", var2)
print("var3:", var3)
print("-" * 30)

# 2. Multiple Assignments to a Single Value
a = b = c = 65
print(f"a = {a}, b = {b}, c = {c}")
print("-" * 30)

# 3. Multiple Values assigned to Multiple Variables (Unpacking)
w, x, y, z = "alpha", "beta", 12, 5.4

# Printing values and checking their types dynamically
print("w:", w, "type:", type(w))
print("x:", x, "type:", type(x))
print("y:", y, "type:", type(y))
print("z:", z, "type:", type(z))

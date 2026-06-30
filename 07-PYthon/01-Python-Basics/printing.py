#!/usr/bin/python3
# Module 1: Python Basics - Printing and String Formatting
# Different ways to output text and variables in Python.

name = "sars_cov_2"
disease = "covid19"

# 1. Comma separation (adds a space automatically between arguments)
print("The name of the virus is", name)

# 2. String format() method (older Python 3 way)
print("The name of the virus is {}".format(name))
print("{} is the name of the virus.".format(name))
print("The name of the virus is {} and it causes {}".format(name, disease))

# 3. F-Strings (Formatted string literals - Modern, clean, and recommended)
print(f"The name of the virus is {name} and it causes {disease}")

# 4. String Concatenation using '+'
print("The name of the virus is " + name)

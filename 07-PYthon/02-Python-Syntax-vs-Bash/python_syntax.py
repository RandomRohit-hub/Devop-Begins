#!/usr/bin/python3
# Module 2: Python Syntax vs Bash - Python Example
# In Python, blocks are defined by indentation (4 spaces) and colons (:).
# There is no 'then' or 'fi'.

x = 2

print("Learning Indentation in Python")
print()

if x == 0:
    print("In the If Block.")
    print("Value of x is 0")
else:
    print("In the else block.")
    print("Value of x is non-zero")

# This print statement must have NO indentation to be outside the else block!
print()
print("This statement is out of the if/else block.")

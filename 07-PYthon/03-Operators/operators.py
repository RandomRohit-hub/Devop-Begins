#!/usr/bin/python3
# Module 3: Operators
# Python uses operators for math, comparisons, and logic.

# 1. Arithmetic Operators
x = 2
y = 7

print("Arithmetic Operators:")
print(f"Addition:       {x} + {y} = {x + y}")
print(f"Subtraction:    {x} - {y} = {x - y}")
print(f"Multiplication: {x} * {y} = {x * y}")
print(f"Division:       {y} / {x} = {y / x}")
print(f"Modulus (rem):  {y} % {x} = {y % x}")
print(f"Exponent (pow): {y} ** {x} = {y ** x}")
print("-" * 30)

# 2. Comparison Operators (Returns True/False)
a = 30
b = 60

print("Comparison Operators:")
print(f"a < b:  {a < b}")
print(f"a > b:  {a > b}")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a >= b: {a >= b}")
print(f"a <= b: {a <= b}")
print("-" * 30)

# 3. Assignment Operators
c = 0
d = 1
print("Assignment Operators:")
print(f"c initial: {c}")
c += d  # Same as c = c + d
print(f"c += d:    {c}")
c -= d  # Same as c = c - d
print(f"c -= d:    {c}")
print("-" * 30)

# 4. Logical Operators (and, or, not)
a = 40
b = 60
x = 2
y = 3

print("Logical Operators:")
print(f"(a < b) or (x > y):  {(a < b) or (x > y)}")   # True or False -> True
print(f"(a > b) or (x < y):  {(a > b) or (x < y)}")   # False or True -> True
print(f"(a > b) or (x > y):  {(a > b) or (x > y)}")   # False or False -> False
print(f"(a > b) and (x < y): {(a > b) and (x < y)}")  # False and True -> False
print(f"(a < b) and (x < y): {(a < b) and (x < y)}")  # True and True -> True
print(f"not(x < y):          {not(x < y)}")           # not True -> False
print("-" * 30)

# 5. Membership Operators (in, not in)
first_tuple = ("IOT", "DevOps", 47, 89, 1.5)
print("Membership Operators:")
print(f"'DevOps' in first_tuple:     {'DevOps' in first_tuple}")
print(f"'DevOps' not in first_tuple: {'DevOps' not in first_tuple}")
print(f"67 not in first_tuple:       {67 not in first_tuple}")
print("-" * 30)

# 6. Identity Operators (is, is not) - checks memory address identity
a = 12
b = 15
print("Identity Operators:")
print(f"a is b:     {a is b}")
print(f"a is not b: {a is not b}")

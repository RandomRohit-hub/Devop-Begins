#!/usr/bin/python3
# Module 4: Conditions
# Decision making in Python using if, elif, and else.

# 1. Simple IF statement
x = 21
if x < 30:
    print("Inside IF block")
    print("X is less than 30")
print("Rest of the code.")
print("-" * 30)

# 2. If/Else statement
x = 31
if x < 30:
    print("Inside if block")
    print("X is less than 30")
else:
    print("Inside else block")
    print("x is greater than or equal to 30")
print("-" * 30)

# 3. If/Elif/Else statement
x = 40
if x > 40:
    print("X is greater than 40")
elif x == 40:
    print("X is equal to 40")
else:
    print("X is less than 40")

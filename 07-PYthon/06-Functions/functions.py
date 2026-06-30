#!/usr/bin/python3
# Module 6: Functions - Basics & Default Arguments
# Functions are reusable blocks of code.

# 1. Function with arguments and return value
def add(arg1, arg2):
    total = arg1 + arg2
    return total

out = add(2, 3)
print("Output from add(2,3):", out)
print("-" * 30)

# 2. Function with arguments and internal print (no explicit return value returns None)
def adder(arg1, arg2):
    total = arg1 + arg2
    print("Inside adder function:", total)

adder(10, 50)
print("Returned value of adder(10,50):", adder(10, 50))  # Prints None
print("-" * 30)

# 3. Function that iterates and sums a list of numbers
def summ(arg):
    x = 0
    for i in arg:
        x = x + i
    return x

out = summ([10, 20, 30])
print("Sum of [10, 20, 30] is:", out)
print("-" * 30)

# 4. Function with Default Arguments
def greetings(MSG="Morning"):
    print(f"Good {MSG}")
    print("Welcome to the function.")

greetings()           # Uses default "Morning"
greetings("Evening")  # Uses provided "Evening"

#!/usr/bin/python3
# Module 8: Exception Handling - Part 2: Try-Except
# Handles ValueError, but if an exception occurs, 'result' is not defined.
# This causes a NameError on line 12 when it tries to print it!

try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Invalid input! Please enter a valid number.")

# WARNING: If ValueError was raised, the variable 'result' was never defined,
# which causes a NameError here!
try:
    print(f"The result is: {result}.")
except NameError as ne:
    print(f"[NameError Caught]: {ne}")

print("This program ends here.")
print("Happy coding.")

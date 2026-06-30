#!/usr/bin/python3
# Module 8: Exception Handling - Part 3: Try-Except-Else
# Solves the NameError from try2.py by printing the result in the 'else' block,
# which only runs if no exception occurred.

try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Invalid input! Please enter a valid number.")
else:
    # This block executes ONLY if no exception occurred in the try block
    print(f"The result is: {result}.")

print("This program ends here.")
print("Happy coding.")

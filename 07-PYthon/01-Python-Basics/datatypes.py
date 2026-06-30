#!/usr/bin/python3
# Module 1: Python Basics - Data Types
# Python has various built-in data types to store different kinds of data.

# 1. Strings (Text) - Single, double, or triple quotes
str1 = "alpha"
str2 = 'beta'
str3 = '''gamma string'''
str4 = """delta string"""

# 2. Numbers (Numeric Types)
num1 = 123  # Integer
flt1 = 2.0  # Float

# 3. List - Ordered, mutable collection of elements, enclosed in square brackets []
first_list = [str1, "DevOps", 47, num1, 1.5]
print("List:", first_list)
print("List type:", type(first_list))
print("-" * 30)

# 4. Tuple - Ordered, immutable collection of elements, enclosed in parentheses ()
first_tuple = (str1, "DevOps", 47, num1, 1.5)
print("Tuple:", first_tuple)
print("Tuple type:", type(first_tuple))
print("-" * 30)

# 5. Dictionary - Key-Value pairs, unordered, mutable, enclosed in curly braces {}
first_dictionary = {
    "Name": "Imran", 
    "Weight": 75, 
    "Exercises": ["Boxing", "Dancing", "Jogging"]
}
print("Dictionary:", first_dictionary)
print("Dictionary type:", type(first_dictionary))
print("-" * 30)

# 6. Boolean - Binary logical state (True or False)
x = True
y = False
print(f"x is {x} ({type(x)})")
print(f"y is {y} ({type(y)})")

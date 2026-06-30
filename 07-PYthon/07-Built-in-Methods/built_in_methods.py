#!/usr/bin/python3
# Module 7: Built-in Methods
# Demonstrates common built-in string, list, and dictionary methods in Python.

# 1. String Methods
message = "corona vaccine is ready to use, most of them are more than 90% effective."
print("Original Message:", message)
print("Capitalized:", message.capitalize())
print("Upper Case: ", message.upper())
print("Is Lower:   ", message.islower())
print("Is Upper:   ", message.isupper())

# Finding substrings and slicing
print("Find index of 'ready':", message.find("ready"))
print("Slice [18:24]:        ", message[18:24])
print("Find index of 'not':  ", message.find("not")) # returns -1 if not found
print("-" * 30)

# Join method
seq1 = ("192", "168", "40", "90")
print("Join with '.':", ".".join(seq1))
print("Join with '/':", "/".join(seq1))
print("Join with '-':", "-".join(seq1))
print("-" * 30)

# 2. List Methods
mountains = ["Everest", "Himalaya", "Sahyadri", "Alps", "K2", "Mt Hood"]
print("Original Mountains:", mountains)

mountains.append("Oregon mount")
print("After append:   ", mountains)

mountains.extend(["Mt Rainer", "Satpuda"])
print("After extend:   ", mountains)

mountains.insert(2, "Mt Abu")
print("After insert(2):", mountains)

mountains.pop() # removes last element
mountains.pop()
mountains.pop()
print("After 3 pops:   ", mountains)

mountains.pop(5) # removes index 5
print("After pop(5):   ", mountains)
print("-" * 30)

# 3. Dictionary Methods
cntr_emp1 = {"Name": "Santa", "Skill": "Blockchain", "Code": 1024}
print("Dictionary keys:  ", list(cntr_emp1.keys()))
print("Dictionary values:", list(cntr_emp1.values()))
cntr_emp1.clear()
print("After clear:      ", cntr_emp1)

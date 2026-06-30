#!/usr/bin/python3
# Module 5: Loops - For and While Loops
# Repeating execution blocks based on collection items or conditions.

# 1. For Loop iterating over a string
PLANET = "Earth"
print("Iterating over string:")
for i in PLANET:
    print("Value of i is now", i)
print("-" * 30)

# 2. For Loop iterating over a tuple
VACCINES_TUPLE = ("Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca")
print("Iterating over tuple:")
for vac in VACCINES_TUPLE:
    print(f"{vac} vaccine provides immunization against COVID-19")
print("-" * 30)

# 3. For Loop iterating over a list
VACCINES_LIST = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca"]
print("Iterating over list:")
for vac in VACCINES_LIST:
    print(f"{vac} vaccine provides immunization against COVID-19")
print("-" * 30)

# 4. While Loop (runs as long as condition is True)
print("Executing while loop:")
x = 0
while x <= 5:
    print(f"Value of X is: {x} (Looping)")
    x += 1
print("Rest of the code (Loop finished).")

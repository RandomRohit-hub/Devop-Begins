#!/usr/bin/python3
# Module 5: Loops - Nested Loops & Infinite Loops
import time

# 1. Nested For Loop (iterates over characters of items in list)
VACCINES = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca"]
for vac in VACCINES:
    print(f"\nI would like to take a shot of: {vac}")
    # Nested loop to print characters of each vaccine name
    for char in vac:
        print(char, end="-")
print("\n" + "-" * 30)

# 2. Infinite While Loop with a multiplier
print("Starting infinite loop demo (with auto-break safety).")
time.sleep(1)
x = 2
while True:
    print("Value of X is:", x)
    x *= 2
    time.sleep(1)
    if x > 1000:
        print("Auto-breaking to avoid infinite output in automated run.")
        break

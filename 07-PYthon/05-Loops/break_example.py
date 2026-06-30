#!/usr/bin/python3
# Module 5: Loops - Break Statement Practical Example
import random

VACCINES = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca", "CoronaVac"]

# Shuffle vaccines list randomly
random.shuffle(VACCINES)
print("Shuffled Vaccines:", VACCINES)

# Pick a random lucky vaccine
LUCKY = random.choice(VACCINES)
print(f"Target successful vaccine to find: {LUCKY}")
print("-" * 30)

for vac in VACCINES:
    print(f"****** TESTING VACCINE: {vac}")
    if vac == LUCKY:
        print("###################################")
        print(f"Success! {LUCKY} Vaccine Test SUCCESSFUL")
        print("###################################\n")
        # Exit the loop immediately since we found the target
        break
    print("XXXXXXXXXXXX")
    print("Test Failed")
    print("XXXXXXXXXXXX\n")

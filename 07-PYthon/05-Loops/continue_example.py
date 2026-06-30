#!/usr/bin/python3
# Module 5: Loops - Continue Statement Practical Example
import random

VACCINES = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca", "CoronaVac"]

# Shuffle vaccines list randomly
random.shuffle(VACCINES)
print("Shuffled Vaccines:", VACCINES)

# Pick a random lucky vaccine
LUCKY = random.choice(VACCINES)
print(f"Target successful vaccine (to skip failure message): {LUCKY}")
print("-" * 30)

for vac in VACCINES:
    print(f"****** TESTING VACCINE: {vac}")
    if vac == LUCKY:
        print("###################################")
        print(f"Success! {LUCKY} Vaccine Test SUCCESSFUL")
        print("###################################\n")
        # Skip the rest of this loop's block and proceed to the next vaccine
        continue
    
    # This block is skipped ONLY when vac == LUCKY
    print("XXXXXXXXXXXX")
    print("Test Failed")
    print("XXXXXXXXXXXX\n")

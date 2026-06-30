#!/usr/bin/python3
# Module 6: Functions - Keyword Arguments
# Demonstrates using keyword arguments to pass parameters regardless of order.

def vac_feedback(vac, efficacy):
    print(f"\n{vac} Vaccine has {efficacy}% efficacy.")
    if (efficacy > 50) and (efficacy <= 75):
        print("Seems not so effective, needs more trials.")
    elif (efficacy > 75) and (efficacy < 90):
        print("Can consider this vaccine.")
    elif efficacy >= 90:
        print("Sure, will take the shot.")
    else:
        print("Needs many more trials.")

# Positional arguments: matches by order
print("Calling with positional arguments:")
vac_feedback("Pfizer", 95)
vac_feedback("Unknown", 45)

# Keyword arguments: matches by name (order doesn't matter)
print("\nCalling with keyword arguments (out of order):")
vac_feedback(efficacy=34, vac="Unknown")

#!/usr/bin/python3
# Module 6: Functions - Modern Module
# This file serves as a helper module containing function definitions
# to be imported and used by other scripts.
import random

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

def order_food(min_order, *args):
    print(f"Required base order: {min_order}")
    for item in args:
        print(f"Additional item ordered: {item}")
    print("Your food will be delivered in 30 mins.")
    print("Enjoy the party!\n")

def time_activity(*args, **kwargs):
    total_minutes = sum(args) + random.randint(0, 60)
    if kwargs:
        choice = random.choice(list(kwargs.keys()))
        print(f"You have to spend {total_minutes} Minutes for {kwargs[choice]} (Category: {choice})")

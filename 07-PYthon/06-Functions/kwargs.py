#!/usr/bin/python3
# Module 6: Functions - Variable Length Keyword Arguments (**kwargs)
# **kwargs allows passing a variable number of keyword arguments as a dictionary.
import random

def time_activity(*args, **kwargs):
    """
    Input: Multiple values for minutes (*args), key=value pairs for activities (**kwargs)
    Output: Prints a random activity and the total minutes spent.
    """
    # args is a tuple of minutes
    # kwargs is a dictionary of activities
    total_minutes = sum(args) + random.randint(0, 60)
    
    # Pick a random activity from kwargs keys
    if kwargs:
        choice = random.choice(list(kwargs.keys()))
        print(f"You have to spend {total_minutes} Minutes for {kwargs[choice]} (Category: {choice})")
    else:
        print(f"You spent {total_minutes} minutes doing nothing.")

print("Calling time_activity:")
time_activity(10, 20, 10, hobby="Dance", sport="Boxing", fun="Driving", work="DevOps")

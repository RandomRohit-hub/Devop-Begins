#!/usr/bin/python3
# Module 6: Functions - Variable Length Arguments (*args)
# *args allows passing a variable number of non-keyword arguments.

def order_food(min_order, *args):
    print(f"Required base order: {min_order}")
    # args is treated as a tuple inside the function
    for item in args:
        print(f"Additional item ordered: {item}")
    print("Your food will be delivered in 30 mins.")
    print("Enjoy the party!\n")

print("Ordering with multiple items:")
order_food("Salad", "Pizza", "Biryani", "Soup")

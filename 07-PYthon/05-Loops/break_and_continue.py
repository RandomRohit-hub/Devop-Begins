#!/usr/bin/python3
# Module 5: Loops - Break and Continue
# 'break' terminates the loop. 'continue' skips to the next iteration.

# 1. Break Statement
print("Testing Break Statement:")
for i in "DevOps":
    print(i)
    if i == "O":
        print("Found character 'O'. Breaking loop!")
        break
print("Out of loop")
print("-" * 30)

# 2. Continue Statement
print("Testing Continue Statement:")
for i in "DevOps":
    if i == "O":
        print("Found character 'O'. Skipping print statement!")
        continue
    print(f"Value of i is {i}")
print("Out of loop")

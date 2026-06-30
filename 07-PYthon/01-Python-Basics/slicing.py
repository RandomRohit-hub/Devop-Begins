#!/usr/bin/python3
# Module 1: Python Basics - Slicing
# Extracting parts of strings, tuples, and lists using indexes and slices.

# 1. String Indexing and Slicing
planet1 = "Closest of Sun"
print("Original String:", planet1)
print("First character (index 0):", planet1[0])
print("Last character (index -1):", planet1[-1])
print("Second to last character (index -2):", planet1[-2])

# Substring extraction: string[start:stop] -> stops before 'stop' index
print("Slice [1:4]:", planet1[1:4])   # "los"
print("Slice [:]:   ", planet1[:])     # Entire string
print("Slice [:7]:  ", planet1[:7])    # Start to index 6: "Closest"
print("Slice [11:]: ", planet1[11:])   # Index 11 to end: "Sun"
print("-" * 30)

# 2. Tuple Indexing and Slicing (Immutable Collection)
devops_tuple = ("Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible")
print("Tuple:", devops_tuple)
print("First element:", devops_tuple[0])
print("Slice [2:5]:  ", devops_tuple[2:5])
print("First element of slice:", devops_tuple[2:5][0])              # "Bash Scripting"
print("Slicing characters in that element:", devops_tuple[2:5][0][5:11])  # "Script"
print("-" * 30)

# 3. List Indexing and Slicing (Mutable Collection)
devops_list = ["Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible"]
print("List:", devops_list)
print("Last element:", devops_list[-1])
print("Slice [2:5]: ", devops_list[2:5])
print("-" * 30)

# 4. Dictionary Lookup & Nested Access
skills = {
    "DevOps": ("AWS", "Jenkins", "Python", "Ansible"), 
    "Development": ["Java", "NodeJS", ".net"]
}
print("Dictionary:", skills)
print("DevOps skills:", skills["DevOps"])
print("Last DevOps skill:", skills["DevOps"][-1])              # "Ansible"
print("First 3 characters of last DevOps skill:", skills["DevOps"][-1][:3])  # "Ans"

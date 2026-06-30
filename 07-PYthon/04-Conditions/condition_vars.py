#!/usr/bin/python3
# Module 4: Conditions - Working with variables and collections
# Checks user inputs against predefined lists, tuples, and dictionaries.

print("This IT Organization has various skill sets.")
print("Find out your match.")
print("Enter Capitalized Values (e.g., Python, Bash, AI): ")

DevOps = ["Jenkins", "Ansible", "Bash", "Python", "Puppet", "Dockers", "Kubernetes", "Terraform"]
Development = ("Nodejs", "Angularjs", "Java", ".net", "Python")
cntr_emp1 = {"Name": "Santa", "Skill": "Blockchain", "Code": 1024}
cntr_emp2 = {"Name": "Rocky", "Skill": "AI", "Code": 1218}

usr_skill = input("Enter your desired skill: ")

# Check in the database if we have this skill
if usr_skill in DevOps:
    print(f"We Have {usr_skill} in DevOps Team.")
elif usr_skill in Development:
    print(f"We have {usr_skill} in Development Team.")
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print(f"We have contract employees with {usr_skill} skill.")
else:
    print("Skill not found")
    print("Please check if you entered the value capitalized or check the spelling.")

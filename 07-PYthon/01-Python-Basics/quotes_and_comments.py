#!/usr/bin/python3
# Module 1: Python Basics - Quotes and Comments
# How to use comments and print string literals with different quotes.

# 1. Single-line Comment: Prefix with '#'

"""
This is a multi-line string used as a comment (docstring).
It uses triple double-quotes.
"""

'''
This is also a multi-line string used as a comment.
It uses triple single-quotes.
'''

skill = "DevOps"
print("skill")  # Prints the literal word "skill"
print('skill')  # Prints the literal word "skill"
print(skill)    # Prints the value stored in the variable 'skill' ("DevOps")

# Triple quotes allow printing text across multiple lines directly
print("""
This is a multi-line paragraph string.
Line 2 of the paragraph.
Line 3 of the paragraph.
""")

print('''
This is also a multi-line paragraph string.
Line 2 of the paragraph.
Line 3 of the paragraph.
''')

# Syntax error example: print(this is a text) -> needs quotes!
print("this is a text")

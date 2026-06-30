#!/bin/bash
# Module 2: Python Syntax vs Bash - Bash Script Example
# This demonstrates block structuring in Bash using 'then' and 'fi',
# and highlights how indentation is optional.

x=0

echo "Learning Indentation in Bash"
echo

if [ $x -eq 0 ]
then
    # Indentation inside this block is just for visual reading, not syntax
    echo "In the If Block."
    echo "Value of x is 0"
else
    echo "In the else block."
    echo "Value of x is non-zero"
fi

echo
echo "This statement is outside of the if/else block."

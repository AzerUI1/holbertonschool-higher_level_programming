#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)  # This is already provided

# Your code starts here
if number > 0:  # Check if the number is greater than 0
    print(f"{number} is positive")
elif number == 0:  # Check if the number is zero
    print(f"{number} is zero")
else:  # If it's not positive or zero, it must be negative
    print(f"{number} is negative")


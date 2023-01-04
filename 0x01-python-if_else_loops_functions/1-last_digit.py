#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
nbr = number
if nbr >= 0:
    nbr = nbr % 10
else :
    nbr = nbr % -10
if nbr >= 6:
    print(f"Last digit of {number} is {nbr} and is greater than 5")
elif nbr < 6 and nbr != 0:
    print(f"Last digit of {number} is {nbr} and is less than 6 and not 0")
else :
    print(f"Last digit of {number} is {nbr} and is 0")

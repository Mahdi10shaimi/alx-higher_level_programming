#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 6 and number != 0:
    last = -(-number % 10)
    print(f"Last degit of {number} is {last} and is less than 6 and not 0")
elif number > 5:
    last1 = number % 10
    print(f"Last degit of {number} is {last1} and is greater than 5")
elif number == 0 :
    last2 = number % 10
    print(f"Last degit of {number} is {last2} and is 0")

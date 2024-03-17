#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last1 = -(-number % 10)
    print(f"Last digit of {number} is {last1} and is less than 6 and not 0")
else:
    last = number % 10
    if last == 0:
        print(f"Last digit of {number} is {last} and is 0")
    else:
        if last < 6:
            print(f"Last digit of {number} is {last} and is less than 6 and not 0")
        elif last > 5:
            print(f"Last dgit of {number} is {last} and is greater than 5")

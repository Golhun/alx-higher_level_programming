#!/usr/bin/python3
import random


number = random.randint(-10000, 10000)


sign = -1 if number < 0 else 1
last_number = (number * sign) % 10
last_number = last_number * sign
message = ""


if last_number > 5:
    message = "and is greater than 5"
elif last_number == 0:
    message = "and is 0"
elif last_number < 6 and last_number != 0:
    message = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last_number} {message}")

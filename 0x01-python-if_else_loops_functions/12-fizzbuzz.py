#!/usr/bin/python3


def fizzbuzz():
    for number in range(1, 100 + 1):
        if number % 5 and number % 3 == 0:
            print("FizzBuZZ", end=", ")
        elif number % 3 == 0:
            print("Fizz", end=", ")
        elif number % 5 == 0:
            print("Buzz", end=", ")
        else:
            print(number, end=", ")

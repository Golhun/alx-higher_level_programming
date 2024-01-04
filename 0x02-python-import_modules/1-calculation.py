#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    ans1 = add(a, b)
    print("{} + {} = {}".format(a, b, ans1))

    ans2 = sub(a, b)
    print("{} - {} = {}".format(a, b, ans2))

    ans3 = mul(a, b)
    print("{} * {} = {}".format(a, b, ans3))

    ans4 = div(a, b)
    print("{} / {} = {}".format(a, b, ans4))

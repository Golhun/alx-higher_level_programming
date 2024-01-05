#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():
    arguments = sys.argv[1:]

    if len(arguments) != 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    a = int(arguments[1])
    operator = arguments[2]
    b = int(arguments[3])

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    main()

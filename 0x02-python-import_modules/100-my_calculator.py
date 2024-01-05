#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():
    arguments = sys.argv[1:]

    if len(arguments) != 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    a = arguments[0]
    operator = arguments[1]
    b = arguments[2]

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Invalid input. <a> and <b> must be integers.")
        sys.exit(1)

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

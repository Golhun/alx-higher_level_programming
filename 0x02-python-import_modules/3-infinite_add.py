#!/usr/bin/python3
import sys


if __name__ == "__main__":
    arguments = sys.argv[1:]
    total = 0

    try:
        if len(arguments) == 0:
            print(f"0")
        else:
            for argument in arguments:
                argument = int(argument)
                total += argument
            print(total)
    except ValueError:
        print("Error: One or more arguments are not valid integers.")

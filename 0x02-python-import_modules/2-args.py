#!/usr/bin/python3
import sys


arguments = sys.argv[1:]
count = 0

if len(arguments) == 0:
    print("0 arguments.")
elif len(arguments) == 1:
    count += 1
    print(f"{len(arguments)} argument:")
    print(f"{count}: {arguments[0]}")
elif len(arguments) > 1:
    print(f"{len(arguments)} arguments:")
    for argument in arguments:
        count += 1
        print(f"{count}: {argument}")

#!/usr/bin/python3


for tens in range(0, 10):
    for ones in range(tens + 1, 10):
        print("{:d}{:d}".format(tens, ones),
              end=", " if tens != 8 or ones != 9 else "\n")

#!/usr/bin/python3


for tens in range(0, 10):
    for ones in range(tens + 1, 10):
        print("{:d}{:d}".format(tens, ones),
              end=", " if tens < 9 or ones < 8 else "\n")

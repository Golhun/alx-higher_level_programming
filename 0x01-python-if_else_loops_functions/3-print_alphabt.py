#!/usr/bin/python3


for ascii_chr in range(97, 122 + 1):
    if ascii_chr not in ["q", "e"]:
        print("{}".format(chr(ascii_chr)), end="")

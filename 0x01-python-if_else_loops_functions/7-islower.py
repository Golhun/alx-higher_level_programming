#!/usr/bin/python3


def islower(c):
    ascii_value = ord(c)
    if ascii_value >= ord("a") and ascii_value <= ord("z"):
        return True
    else:
        return False


print("a => {}".format("lower" if islower("H") else "upper"))
print("H => {}".format("lower" if islower("H") else "upper"))
print("A => {}".format("lower" if islower("H") else "upper"))
print("3 => {}".format("lower" if islower("H") else "upper"))
print("g => {}".format("lower" if islower("H") else "upper"))

#!/usr/bin/python3


def islower(c):
    if not c:
        return False
    
    
    ascii_value = ord(c)
    if ascii_value >= ord("a") and ascii_value <= ord("z"):
        return True
    else:
        return False


print("'' => {}".format("lower" if islower("") else "upper"))
print("a => {}".format("lower" if islower("a") else "upper"))
print("H => {}".format("lower" if islower("H") else "upper"))
print("A => {}".format("lower" if islower("A") else "upper"))
print("3 => {}".format("lower" if islower("3") else "upper"))
print("g => {}".format("lower" if islower("g") else "upper"))

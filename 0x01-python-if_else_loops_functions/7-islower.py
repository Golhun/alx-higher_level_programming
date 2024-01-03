#!/usr/bin/python3


def islower(c):
    if not c:
        return False
    
    
    ascii_value = ord(c)
    if ascii_value >= ord("a") and ascii_value <= ord("z"):
        return True
    else:
        return False
    

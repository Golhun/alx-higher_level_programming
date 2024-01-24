#!/usr/bin/python3

class Square():
    """A class that defines a square with sides"""
    def __init__(self, size=0):
        """Initializing the size property to 0"""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

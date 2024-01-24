#!/usr/bin/python3
"""A python module with a class square"""

class Square():
    """A class that defines a square with sides"""
    def __init__(self, size=0):
        """Initializing the size property and validating it"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """A public method that calculates area of the square and sets it"""
        area = self.__size ** 2
        return area

    @property
    def size(self):
        """A size getter property"""
        square_size = self.__size
        return square_size

    @size.setter
    def size(self, value=0):
        """A size setter for accessing the size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

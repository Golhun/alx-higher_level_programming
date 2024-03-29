#!/usr/bin/python3
"""A python module which creates a square class"""


class Square():
    """A class that defines a square with sides"""
    def __init__(self, size=0):
        """Initializing the size property and validating it"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._size = size

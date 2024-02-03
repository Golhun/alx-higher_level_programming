#!/usr/bin/env python3

"""
A module that adds two integers and returns the answer
"""


def add_integer(a, b=98):
    """
    Function that adds two integers.

    Arguments:
        a (int or float): first int or float.
        b (int or float, optional): second int or float. Defaults to 98.

    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or a float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a + b)

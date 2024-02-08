#!/usr/bin/python3

"""A module containing a function to check if an object is an instance of a specified class."""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if the object is exactly an instance of the specified class; otherwise False.

    """
    return type(obj) is a_class

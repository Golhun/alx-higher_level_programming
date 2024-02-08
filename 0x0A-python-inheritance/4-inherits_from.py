#!/usr/bin/python3

"""A module containing a function to check if an object is an instance of a class inherited from a specified class."""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of a class inherited from the specified class; otherwise False.

    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

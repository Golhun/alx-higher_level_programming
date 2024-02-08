#!/usr/bin/python3
"""
A module that returns attrs and mthd of an object
"""


def lookup(obj):
    """Return list of available attributes and methods of an object"""
    return dir(obj)


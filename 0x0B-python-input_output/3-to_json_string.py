#!/usr/bin/python3
import json

"""
A module that creates a json representation of an object
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """

    return json.dumps(my_obj)


if __name__ == "__main__":
    to_json_string()

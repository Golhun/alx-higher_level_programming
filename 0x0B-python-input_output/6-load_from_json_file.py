#!/usr/bin/python3
"""
A module that creates a python object from a json file
"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The Python data structure represented by the JSON file.
    """

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    load_from_json_file()

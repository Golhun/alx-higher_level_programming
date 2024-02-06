#!/usr/bin/python3
"""
A module that writes to a file
"""


import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized and written to the file.
        filename (str): The name of the file to write to.

    Returns:
        None
    """

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)


if __name__ == "__main__":
    save_to_json_file()

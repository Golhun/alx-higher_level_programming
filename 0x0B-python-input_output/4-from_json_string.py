#!/usr/bin/python3
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Arguments:
        my_str (str): The JSON string representing the object.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)


if __name__ == "__main__":
    from_json_string()

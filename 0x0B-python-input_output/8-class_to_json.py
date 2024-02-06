#!/usr/bin/python3
def class_to_json(obj):
    """
    Returns dict desc with simple data struct
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary representation of the object.
    """

    result = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, bool, int, str)):
            result[key] = value

    return result


if __name__ == "__main__":
    class_to_json()

#!/usr/bin/python3
"""
A module that appends to a file
"""


def append_write(filename="", text=""):
    """
    appends str at the end of a txt file (UTF8), returns number of chars added.

    Arguments:
        filename (str): name of file to append to (default is empty string).
        text (str): text to append to the file (default is empty string).

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)


if __name__ == "__main__":
    append_write()

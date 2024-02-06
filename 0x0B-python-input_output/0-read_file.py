#!/usr/bin/python3
"""
A module that reads a text file
"""


def read_file(filename=""):
    """
    A function that reads a text file (UTF8) and prints it to stdout.

    Arguments passed:
        filename (str): The name of the file to read (default is empty string).

    Returns:
        None
    """

    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")


if __name__ == "__main__":
    read_file()

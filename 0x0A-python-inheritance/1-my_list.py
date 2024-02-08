#!/usr/bin/python3

"""A module containing a class MyList."""


class MyList(list):
    """A custom list class inheriting from the built-in list class."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))

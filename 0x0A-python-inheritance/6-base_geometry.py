#!/usr/bin/python3

"""A module containing a class BaseGeometry."""


class BaseGeometry:
    """A class representing basic geometry operations."""

    def area(self):
        """Calculate the area.

        Raises:
            Exception: Always raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

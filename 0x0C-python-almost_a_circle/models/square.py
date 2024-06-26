#!/usr/bin/python3
"""Defines a Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the Square.
            x (int): The x coordinate of the Square (default 0).
            y (int): The y coordinate of the Square (default 0).
            id (int): The identity of the Square (default None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get or set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square attributes."""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

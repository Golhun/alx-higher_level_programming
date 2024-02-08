#!/usr/bin/python3

"""A module containing a class Rectangle that inherits from BaseGeometry."""


class BaseGeometry:
    """A class representing basic geometry operations."""

    def area(self):
        """Calculate the area.

        Raises:
            Exception: Always raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value as an integer.

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle with the given width and height."""
        self.integer_validator("_Rectangle__width", width)
        self.integer_validator("_Rectangle__height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

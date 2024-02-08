#!/usr/bin/python3

"""A module containing a class Square that inherits from Rectangle."""


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

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height


class Square(Rectangle):
    """A class representing a square, inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a square with the given size."""
        self.integer_validator("_Square__size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

    def area(self):
        """Calculate the area of the square."""
        return self._Rectangle__width * self._Rectangle__height


if __name__ == "__main__":
    import doctest
    doctest.testmod()

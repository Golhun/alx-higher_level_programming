#!/usr/bin/python3
"""
The base class model for all the other classes in the hbnb project
"""


class Base:

    """
    Module serves as the base class for all other classes
    """

    __nb_objects = 0

    def __init__(self, id=none):
        """
        Initializes the base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

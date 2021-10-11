#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """Class

    Atributes:
            area: raises exception

    Raises:
        Exception with error message.

    """

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates value.

        Args:
            name(str)
            value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than zero

        """
        if type(value) is not int:
            raise TypeError(str(name) + ' must be an integer')
        if value <= 0:
            raise ValueError(str(name) + ' must be greater than 0')

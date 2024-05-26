#!/usr/bin/python3
"""Improve Geometry"""


class BaseGeometry:
    """BaseGeometry Class
    Raises Exception
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Value has to be an int"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
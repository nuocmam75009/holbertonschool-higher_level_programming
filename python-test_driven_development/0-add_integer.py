#!/usr/bin/python3

"""Adds two integers"""


def add_integer(a, b=98):

    """
    This function adds 2 integers
    param. a: must be int or float
    param. b: must be int or float
    return: int
    TypeError: if not int or float
    """

    if not isinstance(a, int | float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int | float):
        raise TypeError("b must be an integer")
    else:
        return a + b

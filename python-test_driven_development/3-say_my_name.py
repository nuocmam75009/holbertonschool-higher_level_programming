#!/usr/bin/python3
"""Prints two strings"""

def say_my_name(first_name, last_name=""):
    """function say my name
    values must be strs
    returns str
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))

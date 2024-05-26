#!/usr/bin/python3
"""Checks if object is instance of inherited class"""


def inherits_from(obj, a_class):
    """Returns True if object is instance of inherited class"""
    return isinstance(obj, a_class) and type(obj) is not a_class

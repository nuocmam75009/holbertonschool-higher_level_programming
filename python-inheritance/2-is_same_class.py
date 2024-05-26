#!/usr/bin/python3
"""module that checks if object is exactly an instance of a class"""


def is_same_class(obj, a_class):
    """Returns True if object is instance of specified class"""
    return type(obj) == a_class

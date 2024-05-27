#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """
    function that returns the dict for JSON serialisation
    obj: instance of class
    """
    return obj.__dict__

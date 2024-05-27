#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """
    function that returns the dict for JSON serialisation
    obj: instance of class
    """

    if isinstance(obj, (str, int, bool, list, dict)):
        return {key: value for key, value in obj.__dict__.items()}

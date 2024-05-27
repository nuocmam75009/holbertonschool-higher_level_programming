#!/usr/bin/python3
"""JSON str to object"""


import json


def from_json_string(my_str):
    """
    Function that converts a JSON str to obj
    my_str: JSON string
    Returns: object
    """
    return json.loads(my_str)

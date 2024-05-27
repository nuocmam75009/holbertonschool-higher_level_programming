#!/usr/bin/python3
"""JSON representation"""


import json

def to_json_string(my_obj):
    """
    function that returns JSON representation
    of my_obj
    my_obj: object
    """
    return json.dumps(my_obj)

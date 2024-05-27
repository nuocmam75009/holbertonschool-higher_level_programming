#!/usr/bin/python3
"""write object to txt"""


import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an object to a txt
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return json.dumps(my_obj, f)

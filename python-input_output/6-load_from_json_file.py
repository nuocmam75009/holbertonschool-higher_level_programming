#!/usr/bin/python3
"""json to object"""


import json


def load_from_json_file(filename):
    """
    converts json file to object
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

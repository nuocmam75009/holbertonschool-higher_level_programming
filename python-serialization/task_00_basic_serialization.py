#!/usr/bin/python3

import json


def serialize_and_save_to_file(data, filename):
    """serialize dict to json"""
    json.dump(data, filename)

def load_and_deserialize(filename):
    """deserialize"""
    json.load(filename)

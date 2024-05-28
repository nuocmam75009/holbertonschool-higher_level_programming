#!/usr/bin/python3
import pickle

def serialize_and_save_to_file(data, filename):
    """function that serializes and saves data
    data: python dict
    filename: output JSON file
    """
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_and_deserialize(filename):
    """function that load and deserializes data"""
    with open(filename, 'rb') as f:
        return pickle.load(f)

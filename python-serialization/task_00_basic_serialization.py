import json


def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    json.dump(data, filename)

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    json.load(filename)

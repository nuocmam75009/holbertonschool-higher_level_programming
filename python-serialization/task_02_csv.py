#!/usr/bin/python3
"""CSV to JSON"""


import csv, json

def convert_csv_to_json(csv_filename, data):
    """opens the CSV and reads data
    and then serializes the list of dict
    Error:
    """
    try:
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
            json_data = json.dumps(data)

        with open('data.json', 'w') as json_file:
            """writes serialized JSON to data.json"""
            json_file.write(json_data)
            return True

    except:
        print("Error: File not found")
        return False

# if __name__ == "__main__":
#    convert_csv_to_json("csv_file")
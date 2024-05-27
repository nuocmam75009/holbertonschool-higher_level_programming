#!/usr/bin/python3
"""Write a file"""


def write_file(filename='', text=''):
    """
    function that writes a str to a text file
    filename=file being written
    text=text being added
    Returns number of chars in filename
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)

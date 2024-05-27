#!/usr/bin/python3
"""Append a string"""


def append_write(filename='', text=''):
    """
    Appends a string
    filename=file being appended
    text=string
    Returns: number of chars added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)

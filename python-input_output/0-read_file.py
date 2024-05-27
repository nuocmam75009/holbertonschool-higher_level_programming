#!/usr/bin/python3
"""reads a text file and prints to stdout"""


def read_file(filename=""):
    """
    function that reads a txt file and prints it
    ARG: filename (str)
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')

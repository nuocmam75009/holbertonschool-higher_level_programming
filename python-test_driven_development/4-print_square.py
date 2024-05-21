#!/usr/bin/python3
"""defines a square"""


def print_square(size):
    """
    functions that prints a square
    returns # to print the square
    size must be int and >0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)

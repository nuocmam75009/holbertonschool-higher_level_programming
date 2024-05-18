#!/usr/bin/python3
"""Defines a square"""


class Square:
    """represents a square"""
    def __init__(self, size=0):
        """initializes a square instance
        args:
        size(int) size of the square
        """
        if not isinstance(size, int):
            raise TypeError("value must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

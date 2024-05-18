#!/usr/bin/python3
"""defines a square"""


class Square:
    """represents a square"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("value must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the square's area"""

        return self.__size * self.__size
        # self.__size__ = size

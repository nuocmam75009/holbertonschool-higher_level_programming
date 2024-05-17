#!/usr/bin/python3
class Square:
    def __init__(self, size = 0):
        if not isinstance(size, int):
            raise TypeError("value must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size__ = size

    def area(self):
        return self.__size__ * self.__size__
        # self.__size__ = size

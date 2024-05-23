#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes new rectangle instance
        ARGS:
        width(int)
        height(int)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width of rectangle
        ARGS:
        value(int): width
        RAISES:
        TypeError if not int
        ValueError if < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of rectangle
        ARGS:
        value(int): height
        RAISES:
        TypeError if not int
        ValueError if < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

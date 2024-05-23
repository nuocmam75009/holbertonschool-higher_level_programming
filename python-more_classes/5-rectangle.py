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

    def area(self):
        """returns the area of rectangle (int)"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter
        ARGS:
        int
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns string representation of rectangle with #
        If width or length = 0, return empty string
        """
        if self.__width == 0 or self.__height == 0:
            return ''

        rect_lines = []
        for i in range(self.__height):
            rect_lines.append("#" * self.__width)
        return '\n'.join(rect_lines)

    def __repr__(self):
        """return string repr of rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """prints bye rect when one is deleted"""
        print("Bye rectangle...")

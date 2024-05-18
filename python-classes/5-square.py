#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Get the size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of the value size.
            Args:
                value (int): Value corresponding to the size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self.size == 0:
            print()
            return
        for i in range(self.size):
            for ii in range(self.size):
                print("#", end="")
            print()
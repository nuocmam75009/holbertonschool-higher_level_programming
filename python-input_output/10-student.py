#!/usr/bin/python3
"""pourquoi il faut faire ça"""


class Student:
    """defines a defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dict repr of Student
        attrs: list of strings, only attribute names
        """
        if attrs is None:
            return self.__dict
        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}

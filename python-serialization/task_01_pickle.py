#!/usr/bin/python3
"""Trying out pickle module"""



import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        """declaring variables"""
        self.name = name
        self.age = age
        self.is_student = is_student


        def display(self):
            """display"""
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
            print(f"Is Student: {self.is_student}")

        def serialize(self, filename):
            """serializes into JSON
            handles error if file can't be opened/written
            """
            try:
                with open(filename, "wb") as f:
                    pickle.dump(self, f)
            except Exception:
                print("Error: file cannot be opened or written.")
                return None

        @classmethod
        def deserialize(cls, filename):
            """deserializes
            raises UnpicklingError if data corrupted
            or security violation
            or IOError
            """
            try:
                with open(filename, "rb") as f:
                    return pickle.load(f)
            except (IOError, pickle.UnpicklingError):
                print("Error: File cannot be opened")
                return None

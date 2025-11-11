#!/usr/bin/env python3
"""Serialization and deserialization of custom classes using pickle"""

import pickle


class CustomObject:
    """A simple class for demonstrating object pickling"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object instance to a file"""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a pickle file"""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None

#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """a class that defines a student """
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method def to_json(self, attrs=None): that
        retrieves a dictionary representation of a Student
        instance"""

        if attrs is None:
            return self.__dict__

        else:
            """If attrs is a list of strings, only attribute names
            contained in this list must be retrieved. """
            dict = {}

            for attr in attrs:
                if hasattr(self, attr):
                    dict[attr] = getattr(self, attr)
            return dict

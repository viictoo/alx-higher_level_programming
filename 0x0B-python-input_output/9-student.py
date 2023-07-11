#!/usr/bin/python3
"""Student to JSON """


class Student:
    """a classthat defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method def to_json(self): that retrieves a
        dictionary representation of a Student instance"""
        return self.__dict__

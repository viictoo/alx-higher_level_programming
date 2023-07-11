#!/usr/bin/python3
"""Student to disk and reload """


class Student:
    """a class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary representation
        of a Student instance """
        if attrs is None:
            return self.__dict__
        else:
            dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    dict[attr] = getattr(self, attr)
            return dict

    def reload_from_json(self, json):
        """Public method that replaces all attributes of the Student
        instance
        You can assume json will always be a dictionary
        A dictionary key will be the public attribute name
        A dictionary value will be the value of the public attribute
        """

        for keys in json:
            setattr(self, keys, json[keys])

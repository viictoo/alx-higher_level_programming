#!/usr/bin/python3
""" a function that returns
True if the object is exactly an instance of the specified class
otherwise False
"""


def is_same_class(obj, a_class):
    """Returns:
        Bool: true or false
    """
    return type(obj) == a_class

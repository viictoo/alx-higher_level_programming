#!/usr/bin/python3
"""class to JSON module"""


def class_to_json(obj):
    """a function that returns the dictionary description with
    simple data structure (list, dictionary, string, integer and
    boolean) for JSON serialization of an object:

    Args:
        obj (obj):an instance of a Class

    Returns:
        dict: simple data structure list
    """
    return obj.__dict__

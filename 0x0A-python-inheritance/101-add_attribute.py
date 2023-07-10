#!/usr/bin/python3
"""module to add attribute
"""

def add_attribute(obj, new, value):
    """a function that adds a new attribute to an object if it is possible

    Args:
        obj (class): source to add to
        new (str): obj name
        value (attr): new attribute

    Raises:
        TypeError: cant add new attribute
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, new, value)

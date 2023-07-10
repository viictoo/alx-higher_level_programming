#!/usr/bin/python3


def add_attribute(obj, name, value):
    """a function that adds a new attribute to an object if it’s possible

    Args:
        obj (class): source to add to
        name (str): obj name
        value (attr): new attribute

    Raises:
        TypeError: cant add new attribute
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)

#!/usr/bin/python3
"""to json string module
"""
import json


def to_json_string(my_obj):
    """ function that returns the JSON representation of an object (string)

    Args:
        my_obj (str): python object (string):

    Returns:
        str: JSON string
    """
    return json.dumps(my_obj)

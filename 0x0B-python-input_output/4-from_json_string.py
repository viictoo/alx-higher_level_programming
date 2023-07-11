#!/usr/bin/python3
"""from json string module"""
import json


def from_json_string(my_str):
    """function that returns an object (Python data structure)
    represented by a JSON string:

    Args:
        my_str (str): JSON str

    Returns:
        obj: python object
    """
    return json.loads(my_str)

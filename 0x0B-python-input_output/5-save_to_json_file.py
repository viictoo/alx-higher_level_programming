#!/usr/bin/python3
"""save to json module"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file, using a JSON
    representation:

    Args:
        my_obj (obj): py object
        filename (str): name of dest file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)

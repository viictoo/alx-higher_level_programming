#!/usr/bin/python3
"""load from json file module"""
import json


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file”:

    Args:
        filename (source file): _description_

    Returns:
        obj: python object
    """
    with open(filename, mode="r", encoding="utf-8") as src:
        return json.load(src)

#!/usr/bin/python3
"""This module prints a sentence using two names given
    """


def say_my_name(first_name, last_name=""):
    """Construct the sentence

    Args:
        first_name (string): first name
        last_name (str, optional): last name. Defaults to "".

    Raises:
        TypeError: First name must be a string
        TypeError: Last name must be a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print('My name is', first_name, last_name)

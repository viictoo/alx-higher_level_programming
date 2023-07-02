#!/usr/bin/python3
"""This function adds two integers
"""


def add_integer(a, b=98):
    """adds two integers

    Args:
        a (int): integer
        b (int, optional): integer. Defaults to 98.

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        sum: sum a and b
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b

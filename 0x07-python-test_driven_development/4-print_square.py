#!/usr/bin/python3
"""prints in stdout the square with the character #
"""


def print_square(size):
    """draw the square

    Args:
        size (int): length

    Raises:
        TypeError: size must be an int
        ValueError: size must be greater than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
    if size == 0:
        print('', end='')

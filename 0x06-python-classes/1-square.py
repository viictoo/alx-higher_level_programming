#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """Private instance attribute: size
        Instantiation with size (no type/value verification)
    """
    def __init__(self, size=None):
        self.__size = size

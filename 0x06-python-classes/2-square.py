#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """Private instance attribute: size
       Instantiation with optional int size >= 0
    """
    def __init__(self, size=0):
        """init

        Args:
            size (int, optional): length. Defaults to 0.

        Raises:
            TypeError: not an integer
            ValueError: less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

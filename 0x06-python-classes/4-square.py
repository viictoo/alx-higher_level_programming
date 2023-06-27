#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """Private instance attribute: size
       Instantiation with optional int size >= 0
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """to retrieve size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size to value

        Args:
            value (int): must be >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """public method

        Returns:
            int: size squared
        """
        return self.__size ** 2

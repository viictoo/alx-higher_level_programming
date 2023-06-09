#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """Private instance attribute: size
    """
    def __init__(self, size=0):
        """instatiation

        Args:
            size (int, optional): length. Defaults to 0.

        Raises:
            TypeError: not integer
            ValueError: less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """public intance method

        Returns:
            int: size squared
        """
        return self.__size ** 2

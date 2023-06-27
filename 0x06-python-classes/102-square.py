#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """square
    """
    def __init__(self, size=0):
        """instatiation

        Args:
            size (int): size length. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """getter

        Returns:
            int: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter

        Args:
            value (int): size

        Raises:
            TypeError: not an int
            ValueError: less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """gets area

        Returns:
            int: size squared
        """
        return self.__size ** self.__size

    def __lt__(self, other):
        """less than

        Args:
            other (square): squre

        Returns:
            : comparision of 2 squares
        """
        return self.size < other.size

    def __le__(self, other):
        """less or equal

        Args:
            other (square): squre

        Returns:
            : comparision of 2 squares
        """
        return self.size <= other.size

    def __gt__(self, other):
        """greater than

        Args:
            other (square): squre

        Returns:
            : comparision of 2 squares
        """
        return self.size > other.size

    def __ge__(self, other):
        return self.size >= other.size

    def __eq__(self, other):
        """equal

        Args:
            other (square): squre

        Returns:
            : comparision of 2 squares
        """
        return self.size == other.size

    def __ne__(self, other):
        """not equal

        Args:
            other (square): squre

        Returns:
            : comparision of 2 squares
        """
        return self.size != other.size

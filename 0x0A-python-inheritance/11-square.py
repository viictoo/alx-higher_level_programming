#!/usr/bin/python3
"""Square #2 module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that inherits from Rectangle (9-rectangle.py).

    Args:
        Rectangle (class): class Rectangle
    """
    def __init__(self, size):
        """Instantiation with size

        Args:
            size (int): positive integer, validated by integer_validator
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """[Square] <width>/<height>

        Returns:
            str: the square description: [Square] <width>/<height>
        """
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__size, self.__size)

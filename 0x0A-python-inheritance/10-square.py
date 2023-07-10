#!/usr/bin/python3
"""module for Square #1
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that inherits from Rectangle (9-rectangle.py)

    Args:
        Rectangle (class): rectangle class
    """
    def __init__(self, size):
        """Instantiation with size

        Args:
            size (int): private. No getter or setter
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

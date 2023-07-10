#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry (7-base_geometry.py)"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class Rectangle

    Args:
        BaseGeometry (obj): inherit from
    """
    def __init__(self, width, height):
        """instantiation of values

        Args:
            width (int): width dimension
            height (int): height dimension
        """
        self.integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

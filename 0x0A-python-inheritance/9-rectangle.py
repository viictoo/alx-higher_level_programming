#!/usr/bin/python3
"""module on class rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry (7-base_geometry.py)

    Args:
        BaseGeometry (obj): geometry class
    """
    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area

        Returns:
            int: area = height x width
        """
        return self.__width * self.__height

    def __str__(self):
        """print rectangle descrption

        Returns:
            str: description in a sentence
        """
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)

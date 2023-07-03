#!/usr/bin/python3
""" class Rectangle that defines a rectangle
"""


class Rectangle:
    """set the dimensions
    """
    def __init__(self, width=0, height=0):
        """initial values

        Args:
            width (int, optional): width. Defaults to 0.
            height (int, optional): height. Defaults to 0.
        """
        self.width = width
        self.height = height

    def _check_value(self, value, attr):
        """check for correct values being set

        Args:
            value (int): check value
            attr (str): attribute whose value is being checked

        Raises:
            TypeError: value must be an integer
            ValueError: value must be >= 0
        """
        if type(value) is not int:
            raise TypeError(f"{attr} must be an integer")
        if value < 0:
            raise ValueError(f"{attr} must be >= 0")

    @property
    def width(self):
        """getter for width

        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width

        Args:
            value (int): checked width value
        """
        self._check_value(value, "width")
        self.__width = value

    @property
    def height(self):
        """getter for the height

        Returns:
            int: height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """getter for the height

        Args:
            value (int): new height value
        """
        self._check_value(value, "height")
        self.__height = value

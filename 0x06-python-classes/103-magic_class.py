#!/usr/bin/python3
"""Magic Class

Raises:
    TypeError: integer input only

Returns:
    int: computed values
"""
import math


class MagicClass:
    """Initialize and define methods area and circumference"""
    def __init__(self, radius=0):
        """init magic class

        Args:
            radius (int): radius. Defaults to 0.

        Raises:
            TypeError: radius must be integer
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """area = pi x r squared

        Returns:
            int: area of circle
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """pi x d = circumference
        Returns:
            int: circumference
        """
        return self.__radius * 2 * math.pi

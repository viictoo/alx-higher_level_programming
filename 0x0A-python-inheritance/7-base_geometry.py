#!/usr/bin/python3
"""BaseGeometry Module"""


class BaseGeometry():
    """based on 5-BaseGeometry"""
    def area(self):
        """Public instance method

        Raises:
            Exception: not implemented
        """
        msg = "area() is not implemented"
        raise Exception(msg)

    def integer_validator(self, name, value):
        """Public instance method that validates value

        Args:
            name (str): alias of the value to validate
            value (int): integer

        Raises:
            TypeError: must be an integer
            ValueError: must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

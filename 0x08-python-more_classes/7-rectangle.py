#!/usr/bin/python3
""" class Rectangle that defines a rectangle
"""


class Rectangle:
    """set the dimensions
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initial values

        Args:
            width (int, optional): width. Defaults to 0.
            height (int, optional): height. Defaults to 0.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def area(self):
        """area method

        Returns:
            int: area is height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """perimeter method

        Returns:
            int: 0 if height or width is 0 otherwise
            2(height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.width) * 2

    def __str__(self):
        """print the rectangle with the character #

        Returns:
            string: rect repr using # characters
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        grid = "\n".join([str(self.print_symbol) * self.__width
                          for i in range(self.__height)])
        return grid

    def __repr__(self):
        """ String representation to recreate new instance """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """print string msg if a recanglet is deleted
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

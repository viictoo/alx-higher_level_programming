#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base

    Args:
        Base (cls): Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Private instance attributes, each with its
        own public getter and setter

        Args:
            width (int): width
            height (int): height
            x (int, optional): x axis. Defaults to 0.
            y (int, optional): y axis. Defaults to 0.
            id (int, optional): instace id no. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width

        Returns:
            int: width
        """
        return self.__width

    @property
    def height(self):
        """getter for height

        Returns:
            int: height
        """
        return self.__height

    @property
    def x(self):
        """getter for x

        Returns:
            int: x value
        """
        return self.__x

    @property
    def y(self):
        """getter for y

        Returns:
            int: y value
        """
        return self.__y

    @width.setter
    def width(self, value):
        """setter for width

        Args:
            value (int): width
        """
        self.__validate_integer(value, "width", min=1)
        self.__width = value

    @height.setter
    def height(self, value):
        """setter for height

        Args:
            value (int): height
        """
        self.__validate_integer(value, "height", min=1)
        self.__height = value

    @x.setter
    def x(self, value):
        """setter for x

        Args:
            value (int): x value
        """
        self.__validate_integer(value, "x", min=0)
        self.__x = value

    @y.setter
    def y(self, value):
        """setter for y

        Args:
            value (int): y value
        """
        self.__validate_integer(value, "y", min=0)
        self.__y = value

    @staticmethod
    def __validate_integer(value, name, min):
        """Validates that the value is an integer greater than
        or equal to the specified minimum value."""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value < min:
            if min == 1:
                raise ValueError("{:s} must be > 0".format(name))
            else:
                raise ValueError("{:s} must be >= 0".format(name))

    def area(self):
        """area method

        Returns:
            int: height x width
        """
        return self.__height * self.__width

    def display(self):
        """print in stdout the Rectangle instance with the character #
        by taking care of x and y"""
        for i in range(self.__y + self.__height):
            if i < self.__y:
                print()
            else:
                print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """overrrides the str method to gen a custom string

        Returns:
            str: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[{self.__class__.__name__}] ({self.id})" + \
            f" {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """public method

        Returns:
            dict: returns the dictionary representation of a Rectangle
        """
        dict = {}
        dict['id'] = self.id
        dict['width'] = self.width
        dict['height'] = self.height
        dict['x'] = self.x
        dict['y'] = self.y
        return dict

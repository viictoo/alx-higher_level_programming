#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle

    Args:
        Rectangle (class): parent class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor with parent attributes

        Args:
            size (int): width == height == size
            x (int, optional): x value. Defaults to 0.
            y (int, optional): y value. Defaults to 0.
            id (int, optional): instance id. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size s = s

        Returns:
            int: size = width = height
        """
        return self.width

    @size.setter
    def size(self, value):
        """setter for size

        Args:
            value (int): value
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Prints [Square] (<id>) <x>/<y> - <size>"""
        return f"[{self.__class__.__name__}] ({self.id}) " + \
            f"{self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        # if args:
        # self.id, self.width, self.height, self.x, self.y = args[:5]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation  the

        Returns:
            obj: dictionary
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

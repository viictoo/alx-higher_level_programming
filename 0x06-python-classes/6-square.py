#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """Private instance attribute: size
       Instantiation with optional int size >= 0
    """
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size and optional position

        Args:
            size (int, optional): Defaults to 0.

        Raises:
            ValueError: size is less than 0
            TypeError: size must be an integer
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """to retrieve size attribute"""

        return self.__size

    @size.setter
    def size(self, value):
        """set size to value

        Args:
            value (int): must be >= 0
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter fo Private instance attribute: position

        Returns:
            int: position
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """position setter

        Args:
            value (int): positive integer

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if type(value) is not tuple or len(value) != 2 or\
            type(value[0]) is not int or\
                type(value[1]) is not int or\
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method:
        returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character #
        """

        if self.size == 0:
            print()
        else:
            for i in range(0, self.__position[1]):
                print("")
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end="")
                for k in range(0, self.__size):
                    print("#", end="")
                print("")

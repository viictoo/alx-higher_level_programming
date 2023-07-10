#!/usr/bin/python3
"""MyInt Module(inverted)
"""


class MyInt(int):
    """a class MyInt that inherits from int
    MyInt is a rebel. MyInt has == and != operators inverted
    """
    def __eq__(self, other):
        """(inverted)returns true if not equal
        """
        return int(self) != other

    def __ne__(self, other):
        """(inverted)returns true if equal"""
        return int(self) == other

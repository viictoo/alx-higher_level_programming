#!/usr/bin/python3
"""read file module"""


def read_file(filename=""):
    """a function that reads a text file
    (UTF8) and prints it to stdout:

    Args:
        filename (str, optional): a text file. Defaults to "".
    """
    with open(filename, "r") as f:
        content = f.read()
        print(content, end="")

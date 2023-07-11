#!/usr/bin/python3
"""write file module"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file

    Args:
        filename (str, optional): file to write to/create. Defaults to "".
        text (str, optional): text content. Defaults to "".

    Returns:
        int: the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)

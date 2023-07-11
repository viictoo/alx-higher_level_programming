#!/usr/bin/python3
"""append file module"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8)

    Args:
        filename (str, optional): filename. Defaults to "".
        text (str, optional): content. Defaults to "".

    Returns:
        int: number of characters added:
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)

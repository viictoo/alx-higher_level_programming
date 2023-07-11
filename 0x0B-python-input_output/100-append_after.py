#!/usr/bin/python3
"""Search and Update"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file, after each
    line containing a specific string

    Args:
        filename (str, optional): source file. Defaults to "".
        search_string (str, optional): string to replace. Defaults to "".
        new_string (str, optional): new string. Defaults to "".
    """
    with open(filename, "r") as src:
        text = src.readlines()

    with open(filename, "w") as dest:
        string = ""
        for ln in text:
            string += ln
            if search_string in ln:
                string += new_string
        dest.write(string)

#!/usr/bin/python3
"""module to replace . ? and : in a string of text with newline
"""


def text_indentation(text):
    """format indent in text

    Args:
        text (str): input text string

    Raises:
        TypeError: text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in ".:?":
        text = (char + "\n\n").join(
            [row.strip(" ") for row in text.split(char)])

    print(text, end='')

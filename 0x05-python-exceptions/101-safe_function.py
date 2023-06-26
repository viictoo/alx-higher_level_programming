#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    ret_value = None
    try:
        ret_value = fct(*args)
    except Exception as msg:
        stderr.write("Exception: {}\n".format(msg))
    return ret_value

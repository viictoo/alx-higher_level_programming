#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    pos = 0
    for iter in range(x):
        try:
            print("{:d}".format(my_list[iter]), end="")
            pos += 1
        except (TypeError, ValueError):
            pass
    print()
    return pos

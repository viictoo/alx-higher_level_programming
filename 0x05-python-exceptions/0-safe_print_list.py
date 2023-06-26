#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    pos = 0
    try:
        for iter in range(x):
            print("{}".format(my_list[iter]), end="")
            pos += 1
    except IndexError:
        pass
    finally:
        print()
        return pos

#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key = []
    for x, y in a_dictionary.items():
        if y == value:
            key.append(x)
    for i in key:
        del a_dictionary[i]

    return a_dictionary

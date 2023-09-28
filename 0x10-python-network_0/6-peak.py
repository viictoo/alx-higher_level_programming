#!/usr/bin/python3
""" get the peak int in a list """


def find_peak(list_of_integers):
    """ get highest number in set """
    if len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)

    size = len(list_of_integers)

    mid = size // 2
    peak = list_of_integers[mid]
    if (peak > list_of_integers[mid - 1]) and (
         peak > list_of_integers[mid + 1]):
        return peak
    elif (peak < list_of_integers[mid - 1]):
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])

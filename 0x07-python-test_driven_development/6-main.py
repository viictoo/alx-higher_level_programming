#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

string = [[1, 2, 3, 4], [12, 12, 23, 23]]
print(max_integer(string))
print(max_integer([-1, -1, -1, True]))
print(max_integer([1, 3, 4, float("inf")]))

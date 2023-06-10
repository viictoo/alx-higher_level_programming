#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a0 = 0
    a1 = 0
    b0 = 0
    b1 = 0
    y = len(tuple_a)
    z = len(tuple_b)
    if y > 0:
        a0 = tuple_a[0]
    if y > 1:
        a1 = tuple_a[1]
    if z > 0:
        b0 = tuple_b[0]
    if z > 1:
        b1 = tuple_b[1]
    return a0 + b0, a1 + b1

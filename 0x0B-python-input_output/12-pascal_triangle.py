#!/usr/bin/python3
"""Pascal's Triangle
a triangular arrangement of numbers named after the French
mathematician Blaise Pascal. It starts with a row containing a
single number, which is 1. Each subsequent row is constructed by
adding adjacent numbers from the row above and placing the results
in the current row."""


def pascal_triangle(n):
    """unction def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    eg n = 5
        [1]
        [1,1]
        [1,2,1]
        [1,3,3,1]
        [1,4,6,4,1]

    Args:
        n (int): integer

    Returns:
        list of lists: triangle representation
    """

    if n <= 0:
        return []

    pt = [[1]]
    for _ in range(n-1):
        pt.append([a+b for a, b in zip([0] + pt[-1], pt[-1] + [0])])
    return pt

#!/usr/bin/python3
"""Module that Divides all elements
of a matrix
"""


def matrix_divided(matrix, div):
    """function  that divides matrix elements

    Args:
        matrix (list of lists): matrix of integers or floats
        div (int or float): divisor >= 0

    Raises:
        TypeError: matrix must be a list of lists comprised ints r floats
        ZeroDivisionError: division by 0
        TypeError: each matrix row must have same size
        TypeError: div must be a number >= 0

    Returns:
        matrix: new matrix
    """

    err = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or type(matrix) is not list or matrix is [[]] or \
            len(matrix[0]) == 0:
        raise TypeError(err)

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    quotient = []
    grids = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError(err)
        if len(row) != grids:
            raise TypeError("Each row of the matrix must have the same size")

        temp_l = []
        for elem in row:
            if type(elem) != int and type(elem) != float:
                raise TypeError(err)
            temp_l.append(round(elem/div, 2))
        quotient.append(temp_l)
    return quotient

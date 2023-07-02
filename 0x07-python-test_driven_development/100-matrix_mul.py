#!/usr/bin/python3
"""this module gets the product of a matrix
"""


def matrix_mul(m_a, m_b):
    """matrix multiplication

    Args:
        m_a (list of lists): matrix
        m_b (list of lists): matrix

    Raises:
        ValueError: matrix can't be multiplied if m_b is smaller than m_a

    Returns:
        list of lists: product of m_a and m_b
    """

    error_checker(m_a, "m_a")
    error_checker(m_b, "m_b")

    if len(m_a[0]) > len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
# option 2
# if len(m_a[0]) is not len(m_b):
    #    raise ValueError("other can't be multiplied")

    prod = [[0 for j in range(len(m_b[0]))] for i in range(len(m_a))]
    # move through the rows of a
    for i in range(len(m_a)):
        # move through the elements of b
        for j in range(len(m_b[0])):
            # move to the next row of b
            for k in range(len(m_b)):
                prod[i][j] += m_a[i][k] * m_b[k][j]
    return prod


def error_checker(matrix, name):
    """check for matrix errors

    Args:
        matrix (list of lists): matrix
        name (string): parameter name

    Raises:
        TypeError: matrix must be a list
        ValueError: matrix cant be empty
        TypeError: matrix must be a list of lists
        TypeError: matrix rows must be of the same size
        TypeError: matrix values must only be int of float
    """

    if type(matrix) is not list:
        raise TypeError((name + " must be a list"))

    if not matrix or matrix == [[]]:
        raise ValueError(name + " can't be empty")

    if type(matrix[0]) is not list:
        raise TypeError(name + " must be a list of lists")

    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("each row of " + name
                            + " must be of the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(name +
                                " should contain only integers or floats")

#!/usr/bin/python3
"""multiplication of square matrices using numpy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """function to get the dot product of 2 matrices using matmul

    Args:
        m_a (list of lists): matrix
        m_b (list of lists): matrix

    Returns:
        product: m_a . m_b
    """
    return numpy.matmul(m_a, m_b)

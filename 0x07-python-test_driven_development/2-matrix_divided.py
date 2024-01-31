#!/usr/bin/python3
"""
Module that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.

    Args:
        matrix (list of lists): Matrix of integers or floats.
        div (int or float): The number to divide each element of the matrix.

    Returns:
        list of lists: New matrix with elmts divided by div, rounded to 2 d.p.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                    or if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
        TypeError: If each row of the matrix does not have the same size.
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]

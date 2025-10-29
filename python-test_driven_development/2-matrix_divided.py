#!/usr/bin/python3
"""Modul for divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix"""

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not all(len(matrix[0]) == len(matrix[i]) for i in range(len(matrix))):
        raise TypeError("Each row of the matrix must have the same size")
    new = []
    a = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(a)
            element = round(float(element) / div, 2)
            new_row.append(element)
        new.append(new_row)
    return new

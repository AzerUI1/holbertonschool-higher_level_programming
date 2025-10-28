#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newm = matrix.copy()
    return [list(map(lambda x: x ** 2, row)) for row in newm]

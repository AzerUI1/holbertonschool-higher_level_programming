#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for r in matrix:
            for idx, j in enumerate(r):
                if idx < len(r) - 1:
                    print("{:d}".format(j), end=' ')
                else:
                    print("{:d}".format(j))
    else:
        print()

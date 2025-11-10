#!/usr/bin/python3
"""
This module is for the Pascal's Triangle task
"""


def pascal_triangle(n):
    """
    This function creates a list of lists
    of integers representing the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    pascal = []

    for k in range(n):
        row = [1] * (k + 1)
        for i in range(1, k):
            row[i] = pascal[k - 1][i - 1] + pascal[k - 1][i]
        pascal.append(row)

    return pascal

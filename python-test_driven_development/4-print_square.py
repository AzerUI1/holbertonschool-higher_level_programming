#!/usr/bin/python3
"""Modul for prints a square with the character using '#' """


def print_square(size):
    """ This function that prints a square with the character #."""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print(size * "#")

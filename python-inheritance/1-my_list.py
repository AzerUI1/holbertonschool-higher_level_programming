#!/usr/bin/python3
"""Module for lookup function"""


class MyList(list):
    """Class inherited from list class"""
    def print_sorted(self):
        new = sorted(self)
        print(new)

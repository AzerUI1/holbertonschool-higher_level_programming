#!/usr/bin/python3
"""Module containing is_kind_of_class func"""


def is_kind_of_class(obj, a_class):
    """Module to test the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class"""
    return isinstance(obj, a_class)

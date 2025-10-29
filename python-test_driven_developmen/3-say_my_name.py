#!/usr/bin/python3
"""Modul for prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """A function for prints My name is <first name> <last name>"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name is None:
        raise TypeError("say_my_name() missing 1 required"
                        "positional argument: 'first_name")
    print("My name is {} {}".format(first_name, last_name))

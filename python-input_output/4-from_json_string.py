#!/usr/bin/python3
'''Module that converts a JSON string to an object.'''


def from_json_string(my_str):
    '''Returns a Python object represented by a JSON string'''
    import json
    return json.loads(my_str)

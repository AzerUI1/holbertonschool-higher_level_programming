#!/usr/bin/python3
'''Module that defines a function to read the content of a text file.'''


def to_json_string(my_obj):
    '''Returns the JSON representation of an object (string)'''
    import json
    return json.dumps(my_obj)

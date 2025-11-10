#!/usr/bin/python3
import json
'''Module that defines a function to read the content of a text file.'''

def to_json_string(my_obj):
    '''Returns the JSON representation of an object (string)'''
    return json.dumps(my_obj)

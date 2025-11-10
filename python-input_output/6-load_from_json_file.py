#!/usr/bin/python3
'''Write a function that creates an Object from a JSON file'''


def load_from_json_file(filename):
    '''This function creates an Object from a JSON file'''
    import json
    with open(filename, 'r') as txt_file:
        obj = json.load(txt_file)
        try:
            return obj
        finally:
            txt_file.close()

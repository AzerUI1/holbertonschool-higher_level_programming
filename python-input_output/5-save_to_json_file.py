#!/usr/bin/python3
'''Module that writes an Object to a text file, using a JSON representation'''


def save_to_json_file(my_obj, filename):
    '''Writes an Object to a text file, using a JSON representation'''
    import json
    with open(filename, 'w') as txt_file:
        json.dump(my_obj, txt_file)
        try:
            pass
        finally:
            txt_file.close()

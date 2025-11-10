#!/usr/bin/python3
'''Module that defines a function to write the content of a text file.'''


def write_file(filename="", text=""):
    '''Writes a text into file'''
    with open(filename, 'w', encoding='utf-8') as txt_file:
        content = txt_file.write(text)
        try:
            return content 
        finally:
            txt_file.close() 

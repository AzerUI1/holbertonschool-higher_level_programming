#!/usr/bin/python3
'''Module that defines a function that appends the content of a text file.'''


def append_write(filename="", text=""):
    '''Appends a content to a text file'''
    with open(filename, 'a', encoding='utf-8') as txt_file:
        content = txt_file.write(text)
        try:
            return content
        finally:
            txt_file.close()

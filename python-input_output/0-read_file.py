#!/usr/bin/python3
'''Module that defines a function to read the content of a text file.'''


def read_file(filename=""):
    '''Reads a text file and prints its content to stdout.'''
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        try:
            print(content, end='')
        finally:
            file.close()

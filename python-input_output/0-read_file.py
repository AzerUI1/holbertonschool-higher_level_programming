#!/usr/bin/python3
'''This module defines a function to read and print the content of a text file.'''

def read_file(filename=""):
    """Reads a text file and prints its content to stdout."""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        try:
            print(content, end='')
        finally:
            file.close()

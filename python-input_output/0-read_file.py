#!/usr/bin/env python3

def read_file(filename=""):
    """Reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        try:
            print(content, end='')
        finally: 
            file.close()

#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after each line containing a specific string"""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()  # read all lines

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)  # write the current line
            if search_string in line:  # if it contains the search string
                f.write(new_string)  # insert the new string

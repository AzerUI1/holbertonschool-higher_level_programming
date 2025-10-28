#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = []
    for keys, values in a_dictionary.items():
        new.append(keys)
        new.sort()
    for i in range(0, len(new)):
        print("{}: {}".format(new[i], a_dictionary[new[i]]))

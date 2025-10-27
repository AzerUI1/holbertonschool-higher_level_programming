#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or (idx + 1) > len(my_list):
        return my_list
    else:
        new_list = my_list.copy()
        x = new_list[idx]
        new_list.remove(x)
        new_list.insert(idx, element)
        return new_list

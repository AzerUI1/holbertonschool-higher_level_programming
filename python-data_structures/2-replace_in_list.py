#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or (idx + 1) > len(my_list):
        return my_list
    else:
        x = my_list[idx]
        my_list.remove(x)
        my_list.insert(idx, element)
        return my_list

#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for i in range(0, len(my_list)):
        if my_list[i] == search:
            new.remove(search)
            new.insert(i, replace)
    return new

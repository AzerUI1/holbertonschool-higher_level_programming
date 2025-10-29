#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        len_list = 0
        for i in range(0, x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
                len_list += 1
        print()
        return len_list
    except (TypeError, ValueError):
        print()

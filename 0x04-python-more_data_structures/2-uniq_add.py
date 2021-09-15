#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Function adds unique integers in a list only once."""
    if my_list is not None:
        add = 0
        new_list = set(my_list)
        for i in new_list:
            add = add + i
    return add

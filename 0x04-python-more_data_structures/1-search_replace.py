#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Function that replaces all occurences of an element by another."""
    if my_list is not None:
        new_list = []
        for i in my_list:
            if i == search:
                i = replace
            new_list.append(i)
    return new_list

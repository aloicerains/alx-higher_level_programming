#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Function returns a set of all elements present in one set."""
    new_list = list(set(set_1)-set(set_2))
    new_list2 = list(set(set_2)-set(set_1))
    new_list3 = new_list + new_list2
    return new_list3

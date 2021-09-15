#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Function adds unique integers in a list only once."""
    if set_1 and set_2 is not None:
        new_list = set(set_1).intersection(set_2)
        return new_list

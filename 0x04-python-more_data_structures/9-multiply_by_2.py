#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Function returns new dictionary with values multiplied by 2."""
    if a_dictionary is not None:
        new_di = {}
        for i, j in a_dictionary.items():
            new_di[i] = int(j * 2)
    return new_di

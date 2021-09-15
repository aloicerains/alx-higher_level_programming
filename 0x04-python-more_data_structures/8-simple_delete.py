#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key is not None:
        if key in a_dictionary:
            a_dictionary.pop(str(key))
    return a_dictionary

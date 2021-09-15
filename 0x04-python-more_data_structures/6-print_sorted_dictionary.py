#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Function prints ordered keys in a dictionary."""
    key_s = sorted(a_dictionary.keys())
    length = len(key_s)
    for i in key_s:
        print('{}: {}'.format(i, a_dictionary[i]))

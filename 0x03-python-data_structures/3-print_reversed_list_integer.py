#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Fuction prints all integers of a list in reverse order."""
    size = len(my_list) - 1
    while size >= 0:
        print('{0:d}'.format(my_list[size]))
        size = size - 1

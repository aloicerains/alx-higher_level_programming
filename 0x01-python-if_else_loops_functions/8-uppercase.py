#!/usr/bin/python3
def uppercase(str):
    """Function prints a string in uppercase followed by newline."""
    limit = len(str)
    for i in range(limit):
        if (str[i] >= 'a' and str[i] <= 'z'):
            conversion = ord(str[i]) - 32
            print('{:c}'.format(conversion), end='')
        else:
            print('{}'.format(str[i]), end='')

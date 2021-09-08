#!/usr/bin/python3
def uppercase(str):
    """Function prints a string in uppercase followed by newline."""
    limit = len(str)
    for i in range(limit):
        if (str[i] >= 'a' and str[i] <= 'z'):
            conversion = ord(str[i]) - 32
            if i == limit - 1:
                print('{:c}'.format(conversion))
                break
            print('{:c}'.format(conversion), end='')
        else:
            if i == limit - 1:
                print('{}'.format(str[i]))
                break
            print('{}'.format(str[i]), end='')

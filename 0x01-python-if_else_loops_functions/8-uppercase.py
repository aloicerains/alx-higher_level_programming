#!/usr/bin/python3
def uppercase(str):
    """Function prints a string in uppercase followed by newline."""
    upper = ''
    limit = len(str)
    for i in range(limit):
        if (str[i] >= 'a' and str[i] <= 'z'):
            upper = upper + chr((ord(str[i]) - 32))
        else:
            upper = upper + str[i]
    print(upper)

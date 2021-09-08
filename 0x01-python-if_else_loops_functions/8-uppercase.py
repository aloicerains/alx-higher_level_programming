#!/usr/bin/python3
def uppercase(stri):
    """Function prints a string in uppercase followed by newline."""
    upper = ''
    limit = len(stri)
    for i in range(limit):
        if (stri[i] >= 'a' and stri[i] <= 'z'):
            upper = upper + chr((ord(stri[i]) - 32))
        else:
            upper = upper + stri[i]
    print(upper)

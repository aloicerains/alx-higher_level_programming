#!/usr/bin/python3
def uppercase(str):
    """Function prints a string in uppercase followed by newline."""
    upper = ''
    for i in str:
        char_value = ord(i)
        if ord('a') <= char_value <= ord('z'):
            char_value = char_value - 32
        upper += chr(char_value)
    print("{}".format(upper))

#!/usr/bin/python
"""text_indentation module"""

def text_indentation(text):
    """text_indentation prints two new lines after sysmbols.

    Args:
        text(str): Text document

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    flag = 0
    bsp = ''
    for i in text:
        if i == '.':
            flag = 1
            print(i, end='')        
            continue
        elif i == '?':
            flag = 1
            print(i, end='')
            continue
        elif i == ':':
            flag = 1
            print(i, end='')
            continue
        else:
            if flag == 1:
                print('')
                print('')
            if flag == 1 and i == " ":
                flag = 0
                continue
            print(i, end='')
            flag = 0

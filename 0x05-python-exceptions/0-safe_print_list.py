#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Functin prints x elements of a list."""
    count = 0
    for i in my_list:
        try:
            if count < x:
                print(i, end='')
                count = count + 1
        except RuntimeError:
            raise RuntimeError
    print()
    return count

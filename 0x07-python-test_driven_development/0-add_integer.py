#!/usr/bin/python3
"""0-add_integer module
    The module contains the addition function and raises errors
    if the arguments are not numeric

"""


def add_integer(a, b=98):
    """add_integer adds two integer arguments.

    Args:
        a (int): First argument
        b (int): Second argument

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if either a or b is not an int or a float

    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))

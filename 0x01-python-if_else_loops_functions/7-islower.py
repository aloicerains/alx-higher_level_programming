#!/usr/bin/python3
def islower(c):
    """Determinse if character is lowercase."""
    num = ord(c)
    if num in range(97, 123):
        return True
    else:
        return False

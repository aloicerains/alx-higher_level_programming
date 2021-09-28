#!/usr/bin/python
Square = __import__('0-square').Square


class Square():
    """Square defines the object square using private attribute __size.
    Args:
        __size: Variable argument without specified type.

    Attributes:
        __size: Instance variable of class square.
        .
    """
    def __init__(self, __size):
        self.__size = __size

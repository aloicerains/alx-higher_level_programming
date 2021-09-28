#!/usr/bin/python3
"""Square module - assigns square size and checks for errors."""


class Square:
    """Square defines the object square using private attribute __size.


    Attributes:
        __size: Instance variable of class square.


        """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

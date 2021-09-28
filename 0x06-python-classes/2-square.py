#!/usr/bin/python
class Square:
    """Square defines the object square using private attribute __size.
    Args:
        __size: Variable argument without specified type.

    Attributes:
        __size: Instance variable of class square.

        """
    def __init__(self, __size=0):
        try:
            if not isinstance(__size, int):
                raise TypeError
            if __size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
            return
        except ValueError:
            print("size must be >= 0")
            return
        else:
            self.__size = __size

#!/usr/bin/python3
def raise_exception_msg(message=""):
    """Function raises Name Execption with a message."""
    if message is not None:
        raise NameError(message)

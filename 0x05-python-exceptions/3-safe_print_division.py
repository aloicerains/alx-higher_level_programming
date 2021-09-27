#!/usr/bin/python3
def safe_print_division(a, b):
    """Function divides two integers and prints the result."""
    try:
        x = int(a) / int(b)
    except Exception:
        x = None
    finally:
        if x is not None:
            print("Inside result: {}".format(x))
            return x
        else:
            return None

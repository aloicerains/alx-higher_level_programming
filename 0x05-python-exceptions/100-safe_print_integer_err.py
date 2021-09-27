#!/usr/bin/python3
def safe_print_integer_err(value):
    """Function prints integer and err in stderr."""
    import sys
    try:
        print("{:d}".format(value))
    except TypeError as err:
        sys.stderr.write("Exception: " + str(err) + "\n")
        return False
    except ValueError as er:
        sys.stderr.write('Exception: '+str(er) + '\n')
        return False
    else:
        return True

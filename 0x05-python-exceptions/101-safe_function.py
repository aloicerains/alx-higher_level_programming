#!/usr/bin/python3
def safe_function(fct, *args):
    """Function that executes a function safely."""
    import sys
    if fct is not None and args is not None:
        try:
            fct(*args)
        except Exception as ex:
            sys.stderr.write('Exception: ' + str(ex) + '\n')
            return None
        else:
            return fct(*args)

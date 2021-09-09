#!/usr/bin/python3
if __name__ == "__main__":
    from inspect import getmembers, isfunction
    import hidden_4
    for k, v in getmembers(hidden_4, isfunction):
        if k.startswith('__') is False:
            print(k)

#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lists = sys.argv
    args = len(lists) - 1
    if args == 0:
        print('{} arguments.'.format(0))
    elif args == 1:
        print('{} argument:'.format(1))
        print('{}: {}'.format(1, lists[1]))
    elif args > 1:
        print('{} arguments:'.format(args))
        for i in range(1, args + 1):
            print('{}: {}'.format(i, lists[i]))

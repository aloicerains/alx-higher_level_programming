#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lists = sys.argv
    args = len(lists) - 1
    if args == 0:
        print('{}'.format(0))
    elif args == 1:
        print('{}'.format(lists[1]))
    elif args > 1:
        result = 0
        for i in range(1, args + 1):
            result = result + int(lists[i])
        print('{}'.format(result))

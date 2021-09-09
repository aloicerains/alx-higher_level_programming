#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    lists = sys.argv
    args = len(lists) - 1
    if args != 3:
        print('Usage: {} <a> <operator> <b>'.format(lists[0]))
        sys.exit(1)
    op = ['+', '-', '*', '/']
    a = int(lists[1])
    b = int(lists[3])
    j = 0
    for i in range(4):
        if lists[2] == op[i]:
            break
        j = j + 1
    if lists[2] != op[i]:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
    if j == 0:
        print('{} + {} = {}'.format(a, b, add(a, b)))
    elif j == 1:
        print('{} - {} = {}'.format(a, b, sub(a, b)))
    elif j == 2:
        print('{} * {} = {}'.format(a, b, mul(a, b)))
    elif j == 3:
        print('{} / {} = {}'.format(a, b, div(a, b)))

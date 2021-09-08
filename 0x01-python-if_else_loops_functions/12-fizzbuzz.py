#!/usr/bin/python3
def fizzbuzz():
    """Function prints the formated numbers 1 to 100."""
    for i in range(1, 101):
        if i % 15 == 0 and i < 100:
            print('FizzBuzz', end=', ')
            continue
        elif i % 5 == 0 and i < 100:
            print('Buzz', end=', ')
            continue
        elif i % 3 == 0 and i < 100:
            print('Fizz', end=', ')
            continue
        elif i < 100:
            print(i, end=', ')
        else:
            print('Buzz', end='')

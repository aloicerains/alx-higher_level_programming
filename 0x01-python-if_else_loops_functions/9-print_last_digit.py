#!/usr/bin/python3
def print_last_digit(number):
    """Function prints last digit of a number."""
    if number < 0:
        last_digit = abs(number) % 10
    else:
        last_digit = number % 10
    print(last_digit, end="")
    return last_digit

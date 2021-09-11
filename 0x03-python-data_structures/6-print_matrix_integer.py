#!/usr/bin/pthon3
def print_matrix_integer(matrix=[[]]):
    """Function prints a matrix of integers."""
    for row in matrix:
        for i in row:
            print('{}'.format(i), end=" ")
        print()

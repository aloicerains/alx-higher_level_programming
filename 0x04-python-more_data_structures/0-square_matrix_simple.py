#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Function computes the square value of all integers of a matrix."""
    if matrix is not None:
        square = [[i**2 for i in row] for row in matrix]
        return square

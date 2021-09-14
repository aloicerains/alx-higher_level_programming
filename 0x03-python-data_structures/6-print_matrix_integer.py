def print_matrix_integer(matrix=[[]]):
    """Function prints a matrix of integers."""
    for row in matrix:
        for i in row:
            if i == row[len(row) - 1]:
                print("{:d}".format(i))
                continue
            print('{:d}'.format(i), end=" ")
    if len(row) == 0:
        print()

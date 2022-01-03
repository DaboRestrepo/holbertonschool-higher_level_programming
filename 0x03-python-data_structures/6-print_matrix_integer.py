#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for row in matrix:
            print(' '.join('{:d}'.format(item) for item in row))

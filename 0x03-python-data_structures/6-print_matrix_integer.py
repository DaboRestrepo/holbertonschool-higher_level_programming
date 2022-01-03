#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for i in matrix:
            print('{}'.format(' '.join(map(str, i))))

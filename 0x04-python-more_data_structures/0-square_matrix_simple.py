#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        square = [[item ** 2 for item in row] for row in matrix]
        return square

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = [[(row[item] ** 2) for item in range(3)] for row in matrix]
    return square

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = [[(row[item] ** 2) for row in matrix] for item in range(3)]
    return square

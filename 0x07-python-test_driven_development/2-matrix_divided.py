#!/usr/bin/python3
"""
This is matrix_dicided module:

This supplies one function, matrix_divided
"""


def matrix_divided(matrix, div):
    """This function divide the matrix elements by the int/float div
    >>> matrix_divided(matrix, 3)
    [[(eleme/3)], [eleme/3]]"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if not isinstance(j, (int, float)):
                raise TypeError(
                  "matrix must be a matrix (list of lists) of integers/floats")
    new_matrix = [[float('{:.2f}'.format(row[item] / div)) for item in
                   range(len(matrix[0]))] for row in matrix]
    return new_matrix

#!/usr/bin/python3
"""
This is the module print_square:

This supplie one function named print_square
"""


def print_square(size):
    """This function print a square made of # symbols
    >>> print_square(2)
    ##
    ##"""
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()

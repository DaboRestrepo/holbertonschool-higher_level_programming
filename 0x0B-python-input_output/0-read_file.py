#!/usr/bin/python3
"""This module supplies the function read_file"""


def read_file(filename=""):
    """This functions allows us to read the giving file.
    Args:
    - filename: the file to be read."""
    with open(filename, 'r') as file:
        for line in file:
            print(line, end='')

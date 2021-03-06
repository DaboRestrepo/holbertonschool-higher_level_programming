#!/usr/bin/python3
"""This module supplies the function write_file"""


def write_file(filename="", text=""):
    """This function allows us to write in an existing or non file"""
    with open(filename, 'w') as file:
        return file.write(text)

#!/usr/bin/python3
"""This module supplies the function append_write"""


def append_write(filename="", text=""):
    """This function append text to the file
    Args:
    - filename: file to be append.
    - text to write in the file"""
    with open(filename, 'a') as file:
        return file.write(text)

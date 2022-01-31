#!/usr/bin/python3
"""Function that list the attributes and methods"""


def lookup(obj):
    """Function to return a list of the available attributes and methods of
    the object.
    Args:
        -obj: the giving object."""
    my_list = dir(obj)
    return my_list

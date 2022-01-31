#!/usr/bin/python3
def lookup(obj):
    """Function to return a list of the available attributes and methods of
    the object.
    Args:
        -obj: the giving object."""
    return dir(obj)

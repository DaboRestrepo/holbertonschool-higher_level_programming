#!/usr/bin/python3
"""Function that evaluate an object type"""


def is_same_class(obj, a_class):
    """This return True if the object is exactly an instance of a class.
    Args:
    - obj: object that is being studing
    - a_class: the givind class"""
    if type(obj) == a_class:
        return True
    return False

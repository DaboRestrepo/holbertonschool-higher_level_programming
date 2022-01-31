#!/usr/bin/python3
"""Function that evaluates the instance type"""


def is_kind_of_class(obj, a_class):
    """Return True when object is an instance of a class that inherited from.
    Args:
    - obj: object that is being studing
    - a_class: the givind class"""
    return (isinstance(obj, a_class))

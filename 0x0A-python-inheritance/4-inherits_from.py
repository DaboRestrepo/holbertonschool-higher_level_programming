#!/usr/bin/python3
"""This supplies the inherits_from function"""


def inherits_from(obj, a_class):
    """Determine if the object inherites of the class"""
    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)

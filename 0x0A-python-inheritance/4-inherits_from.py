#!/usr/bin/python3
"""This supplies the inherits_from function"""


def inherits_from(obj, a_class):
    """Determine if the object inherites of the class"""
    if isinstance(obj, a_class) and type(obj) is a_class:
        return False
    return True

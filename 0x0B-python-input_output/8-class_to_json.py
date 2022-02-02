#!/usr/bin/python3
"""This module supplies the funcion class_to_json"""


def class_to_json(obj):
    """This function returns a dict
    Args:
    - obj: Giving obj."""
    return obj.__dict__

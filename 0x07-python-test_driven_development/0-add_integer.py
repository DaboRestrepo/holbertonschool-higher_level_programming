#!/usr/bin/python3
"""
This is add_ integer module:

This supplies one function, add_integer().
"""


def add_integer(a, b=98):
    """Function that add two integers. Example:
        >>> add_integer(1, 2)
        3"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)

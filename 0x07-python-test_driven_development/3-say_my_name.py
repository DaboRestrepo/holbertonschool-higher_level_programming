#!/usr/bin/python3
"""
This is say_my_name module:

This supplies one function named say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """This function print the string "My name is" with the giving strings.
    >>> say_my_name("Daniela", "Botero")
    My name is Daniela Botero"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

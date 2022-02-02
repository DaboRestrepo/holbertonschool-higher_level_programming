#!/usr/bin/python3
"""This module supplies the function to_json_string"""

import json


def to_json_string(my_obj):
    """This function allows to print the str way of the object.
    Args:
    - my_obj: the giving object."""
    return json.dumps(my_obj)

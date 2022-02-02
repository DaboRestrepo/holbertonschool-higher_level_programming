#!/usr/bin/python3
"""This module supplies the function from_json_string"""

import json


def from_json_string(my_str):
    """This function decodes the str.
    Args:
    - my_str: the str to decode."""
    return json.loads(my_str)

#!/usr/bin/python3
"""This module supplies the save_to_json_file function"""

import json


def save_to_json_file(my_obj, filename):
    """This function save the str obj in the file.
    Args:
    - my_obj: object to transform.
    -filename: file to save the obj."""
    with open(filename, 'w') as file:
        return json.dump(my_obj, file)

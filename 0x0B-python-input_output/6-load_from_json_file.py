#!/usr/bin/python3
"""This module supplies the load_from_json_file function"""


import json


def load_from_json_file(filename):
    """This function allows us to create an obj from a Json file
    Args:
    - filename: json file."""
    with open(filename, 'r+') as file:
        return json.load(file)

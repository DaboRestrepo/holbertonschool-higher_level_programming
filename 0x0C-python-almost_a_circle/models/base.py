#!/usr/bin/python3
"""This module soport the base class"""

import json


class Base:
    """Base class of the"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the id attribute
        Args:
        - id: integer type argument."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the Json string representation"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the string representation of the json file"""
        if json_string is not None:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """Save the list in a json file"""
        file = (cls.__name__ + ".json")
        with open(file, 'w') as fd:
            if list_objs is None:
                fd.write('[]')
            fd.write(cls.to_json_string([item.to_dictionary() for item in
                                        list_objs]))

    @classmethod
    def create(cls, **dictionary):
        """Returns all instances with attr set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(8, 3, 2)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(dictionary)
        return dummy

#!/usr/bin/python3
"""This module supplies the class Student"""


class Student:
    """In this class is the to_json function"""
    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the data in dictionary way"""
        if type(attrs) is list:
            data = {"first_name": self.first_name,
                    "last_name": self.last_name, "age": self.age}
            return {element: data[element] for element in attrs if
                    type(element) is str and element in data.keys()}
        return self.__dict__

    def reload_from_json(self, json):
        """Reload the jsondictionary"""
        self.__dict__ = json

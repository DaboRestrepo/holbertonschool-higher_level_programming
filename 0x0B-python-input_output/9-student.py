#!/usr/bin/python3
"""This module supplies the class Student"""


class Student:
    """In this class is the to_json function"""
    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the data in dictionary way"""
        return self.__dict__

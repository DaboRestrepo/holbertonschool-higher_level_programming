#!/usr/bin/python3
"""This module supplies the class Student"""
Student = __import__('10-student').Student


def reload_from_json(self, json):
    """Reload the json dictionary"""
    self.__dict__ = json

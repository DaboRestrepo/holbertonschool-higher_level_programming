#!/usr/bin/python3
"""Tha BaseGeometry class

This supplies the area and the integer_validator functions"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class inherates from BaseGeometry Class"""
    def __init__(self, width, height):
        """Inicialize the width and height values"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

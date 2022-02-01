#!/usr/bin/python3
"""Tha BaseGeometry class

This supplies the area and the integer_validator functions"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class supplies the instantation with size"""
    def __init__(self, size):
        """Instantiation with size"""
        self.__size = size
        self.integer_validator("size", self.__size)
        Rectangle.__init__(self, width=self.__size, height=self.__size)
        Rectangle.area(self)

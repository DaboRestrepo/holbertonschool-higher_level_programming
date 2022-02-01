#!/usr/bin/python3
"""Tha BaseGeometry class

This supplies the area and the integer_validator functions"""


from lib2to3.pytree import Base


class BaseGeometry:
    """Empty class BaseGeometry"""
    def area(self):
        """Function to raise and Exception error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Evaluate the value type and value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


bg = BaseGeometry()


class Rectangle(BaseGeometry):
    """This class inherates from BaseGeometry Class"""
    def __init__(self, width=0, height=0):
        """Inicialize the width and height values"""
        self.__width = width
        self.__height = height
        bg.integer_validator("width", self.__width)
        bg.integer_validator("height", self.__height)

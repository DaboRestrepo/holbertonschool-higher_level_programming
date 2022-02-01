#!/usr/bin/python3
"""Tha BaseGeometry class

This supplies the area and the integer_validator functions"""


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
    def __init__(self, width, height):
        """Inicialize the width and height values"""
        self.__width = width
        self.__height = height
        bg.integer_validator("width", self.__width)
        bg.integer_validator("height", self.__height)

    def __str__(self):
        """This function implement the magic class str"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Return the rectangle area"""
        return self.__width * self.__height


class Square(Rectangle):
    """This class supplies the instantation with size"""
    def __init__(self, size):
        """Instantiation with size"""
        self.__size = size
        bg.integer_validator("size", self.__size)
        Rectangle.__init__(self, width=self.__size, height=self.__size)
        Rectangle.area(self)

    def __str__(self):
        """This function implement the magic class str in Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)

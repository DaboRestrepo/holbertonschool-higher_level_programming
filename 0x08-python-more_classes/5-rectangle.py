#!/usr/bin/python3
"""
This is the rectangle module:

This supplies the rectangle function.
"""


class Rectangle:
    """This class set the rectangle features"""
    def __init__(self, width=0, height=0):
        """Inicialize the rectangle variables
        Args:
        - width is one size of the rectangle.
        - height is the other size of the rectangle"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """Set the size of the height variable"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the new propieties of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """Set the size of the width variable"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the new propieties of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """Calculate the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculate the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Special method to print the object"""
        if self.width == 0 or self.height == 0:
            return ""
        rec_w = "#" * self.width
        rec = rec_w
        for hei in range(self.height - 1):
            rec += '\n' + rec_w
        return rec

    def __repr__(self):
        """Special method to represent the object"""
        rec = '{self.__class__.__name__}({self.width}, {self.height})'\
              .format(self=self)
        return rec

    def __del__(self):
        """Finalizer of the rectangle class"""
        print("Bye rectangle...")

#!/usr/bin/python3
"""Empty class BaseGeometry"""


class BaseGeometry:
    """Empty class BaseGeometry"""
    def area(self):
        """Function to raise and Exception error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Evaluate the value type and value"""
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")

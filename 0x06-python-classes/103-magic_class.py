#!/usr/bin/python3
"""Class to know the area and circumference"""
import math


class MagicClass:
    """Class to define the area and the circumference"""
    def __init__(self, radius=0):
        """Inicialize the radius variable"""
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate the area importing pi from math"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculate the circumference importing pi from math"""
        return 2 * math.pi * self.__radius

import dis
dis.dis(MagicClass)
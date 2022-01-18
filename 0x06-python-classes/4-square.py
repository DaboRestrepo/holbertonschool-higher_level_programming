#!/usr/bin/python3
"""Class Square definition"""


class Square:
    """Class that defines a square:

    Atributes:
        - Private attribute size: is the size of a side.
    """
    def __init__(self, size=0):
        """Inicialize a square

        Args:
            - size (int): the size of the sides."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Define the square area:

        Return:
            The size by 2."""
        return self.__size ** 2

    @property
    def size(self):
        """Set the new value for the size

        Return:
            The new size."""
        return self.__size

    @size.setter
    def size(self, size):
        """Set the value in the property

        Args:
            size (int): new size of the size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

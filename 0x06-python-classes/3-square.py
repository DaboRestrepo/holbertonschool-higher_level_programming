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

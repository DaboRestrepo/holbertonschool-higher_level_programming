#!/usr/bin/python3
"""Class Square definition"""


class Square:
    """Class that defines a square:

    Atributes:
        - Private attribute size: is the size of a side.
    """
    def __init__(self, size):
        """Inicialize a square

        Args:
            - size (int): the size of the sides."""
        self.__size = size

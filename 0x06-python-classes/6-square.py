#!/usr/bin/python3
"""Class Square definition"""


class Square:
    """Class that defines a square:

    Atributes:
        - Private attribute size: is the size of a side.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Inicialize a square

        Args:
            - size (int): the size of the sides.
            - position (tuple): the position in the tuple"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Set the new value for the size

        Return:
            The new size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value in the property

        Args:
            value (int): new size of the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Define the square area:

        Return:
            The size by 2."""
        return self.__size ** 2

    def my_print(self):
        """Print a # for index in the size"""
        if self.size != 0:
            for h in range(self.position[1]):
                print()

            for i in range(self.size):
                for j in range(self.position[0]):
                    print(" ", end="")
                for k in range(self.size):
                    print("#", end="")
                print()
        else:
            print()

    @property
    def position(self):
        """Set the position

        Return:
            position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the value in the property

        Args:
            - value (tuple): the tuple with the numbers"""
        if not isinstance(value, tuple) or len(value) != 2 \
           or not isinstance(value[0], int) or not isinstance(value[1], int)\
           or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

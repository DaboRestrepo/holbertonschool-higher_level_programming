#!/usr/bin/python3
"""This module soport the Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class build a square. It inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the attributes with the Rectangle attrs:
        Args:
        width and height: has the same size.
        x: the space up the rectangle.
        y: the space at the left of the square"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.__size = size

    def __str__(self):
        """Print the Square information"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """The getter of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """The setter of size"""
        if not isinstance(value, int):
            raise TypeError("widht must be an integer")
        elif value <= 0:
            raise ValueError("widht must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """This function update the Square information
        Args:
        - args: the list of arguments.
        - kwargs: the key and value list."""
        if len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except Exception:
                pass
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id' and value != 0:
                    self.id = value
                elif key == 'size' and value != 0:
                    self.size = value
                elif key == 'x' and value != 0:
                    self.x = value
                elif key == 'y' and value != 0:
                    self.y = value

    def to_dictionary(self):
        """This function return the Square dict representation"""
        obj = self.__dict__
        print(obj)
        obj['x'] = obj.pop('_Rectangle__x')
        obj['size'] = obj.pop('_Square__size')
        obj['y'] = obj.pop('_Rectangle__y')
        obj.pop('_Rectangle__height')
        obj.pop('_Rectangle__width')
        return obj

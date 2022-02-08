#!/usr/bin/python3
"""This module soport the class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """This class inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle class with:
        Args:
        width: the size of one side.
        height: the size of other side.
        x: the space up the rectangle.
        y: the space at the left of the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """The getter of the private width"""
        return self.__width

    @width.setter
    def width(self, value):
        """The setter of the private width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """The getter of the private height"""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter of the private height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """The getter of the private x"""
        return self.__x

    @x.setter
    def x(self, value):
        """The setter of the private x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """The getter of the private y"""
        return self.__y

    @y.setter
    def y(self, value):
        """The setter of the private y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """This function provides the Rectangle area"""
        return self.__width * self.__height

    def display(self):
        """This function print the Rectangle with #"""
        for line in range(self.__y - 1):
            print("\n")
        str1 = (" " * self.__x) + ("#" * self.__width)
        str2 = str1
        for column in range(self.__height - 1):
            str2 += "\n" + str1
        print(str2)

    def __str__(self):
        """This function print the Rectangle information"""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """This function update the Rectangle information
        Args:
        - args: the list of arguments.
        - kwargs: the key and value list."""
        if len(args) != 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except Exception:
                pass
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id' and value != 0:
                    self.id = value
                elif key == 'width' and value != 0:
                    self.width = value
                elif key == 'height' and value != 0:
                    self.height = value
                elif key == 'x' and value != 0:
                    self.x = value
                elif key == 'y' and value != 0:
                    self.y = value

    def to_dictionary(self):
        """This function return the Rectangle dict representation"""
        obj = self.__dict__
        obj['x'] = obj.pop('_Rectangle__x')
        obj['y'] = obj.pop('_Rectangle__y')
        obj['id'] = obj.pop('id')
        obj['height'] = obj.pop('_Rectangle__height')
        obj['width'] = obj.pop('_Rectangle__width')
        return obj

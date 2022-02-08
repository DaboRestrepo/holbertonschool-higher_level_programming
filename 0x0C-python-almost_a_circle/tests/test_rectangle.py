#!/usr/bin/python3
"""This module soport the TestRectangle class"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """This class test the rectangle class"""
    def Test_init(self):
        """Test the initialize attr"""
        r1 = Rectangle(5)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        r3 = Rectangle(23, 9, 78, 3, 6)
        self.assertEqual(r3.id, 6)
        self.assertEqual(r3.y, 3)
        r4 = Rectangle(23, 9, 78, 3, (2, 3))
        self.assertEqual(r4.id, (2, 3))
        r5 = Rectangle(23, 9, 78, 3, {"Hola": 4})
        self.assertEqual(r5.id, {"Hola": 4})
        r6 = Rectangle(23, 9, 78, 3, ["Hola"])
        self.assertEqual(r6.id, ["Hola"])
        r6 = Rectangle(23, 9, 78, 3, "Hola")
        self.assertEqual(r6.id, "Hola")
        r7 = Rectangle(23, 9, 78, 3, None)
        self.assertEqual(r7.id, 2)

    def Test_Raises(self):
        """Test the errors"""
        with self.assertRaises(TypeError):
            Rectangle("Hola", 5)
            Rectangle(5, "Hola")
            Rectangle([2, 3], 5)
            Rectangle(5, [2, 3])
            Rectangle({"width": 5}, 5)
            Rectangle(5, {"height": 5})
            Rectangle()
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
            Rectangle(1, -2)
            Rectangle(0, 1)
            Rectangle(1, 0)
            Rectangle(1, 2, -3)
            Rectangle(1, 2, 3, -4)
            Rectangle(None)

    def Test_Area(self):
        """Test the area function"""
        ar1 = Rectangle(2, 5)
        self.assertEqual(ar1.area, 10)
        ar2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(ar2.area, 2)

    def Test_Display(self):
        """Test the display function"""
        dr1 = Rectangle(1, 2)
        display = "#\n#\n"
        self.assertEqual(dr1.display, display)
        dr2 = Rectangle(2, 3, 1, 1)
        display = "\n #\n #\n"
        self.assertEqual(dr2.display, display)

    def Test_str(self):
        """Test the str function"""
        st1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(st1, "[Rectangle] (5) 3/4 - 1/2")
        st2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(st2, "[Rectangle] (1) 3/4 - 1/2")
        st3 = Rectangle(1, 2, 3)
        self.assertEqual(st3, "[Rectangle] (2) 3/0 - 1/2")

    def Test_update(self):
        """Test the update args and kwargs"""
        up1 = Rectangle(10, 10, 10, 10)
        up1.update(89)
        self.assertEqual(up1, "[Rectangle] (89) 10/10 - 10/10")
        up1.update(89, 1, 2, 3, 4)
        self.assertEqual(up1, "[Rectangle] (89) 3/4 - 1/2")
        up1.update(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(up1, "[Rectangle] (89) 3/4 - 1/2")

    def Test_Dict(self):
        """Test to dictionary function"""
        dic1 = Rectangle(1, 2, 3, 4, 5)
        dic1_dictionary = dic1.to_dictionary()
        self.assertEqual(dic1_dictionary, "{'x': 3, 'y': 4, 'id': 5,\
                                           'height': 2, 'width': 1}")
        dic2 = Rectangle(1, 2, 3, 4)
        dic2.update(**dic1_dictionary)
        self.assertEqual(dic1_dictionary, "{'x': 3, 'y': 4, 'id': 1,\
                                           'height': 2, 'width': 1}")


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""This module soport the class TestSquare"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test the Square class"""
    def test_heritance(self):
        """Test all the Square functions"""
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1, "[Square] (4) 2/3 - 1")
        self.assertEqual(s1.area, 1)
        self.assertEqual(s1.display, "\n\n\n  #\n  #\n")
        self.assertEqual(s1.size, 1)
        s1.size = 8
        self.assertEqual(s1.size, 8)
        s1.update(10)
        self.assertEqual(s1, "[Square] (10) 2/3 - 1")
        s1.update(5, 6, 7, 7)
        self.assertEqual(s1, "[Square] (6) 7/7 - 6")
        s1.update(id=7, size=7, x=6, y=5)
        self.assertEqual(s1, "[Square] (7) 6/5 - 7")
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, "[Square] (7) 6/5 - 7\n\
                                         {'id': 7, 'x': 6, 'size': 7, 'y': 5}")

    def test_errors(self):
        """Test the raising errors and exceptions"""
        with self.assertRaises(TypeError):
            Square("Hola", 5)
            Square(5, "Hola")
            Square([2, 3], 5)
            Square(5, [2, 3])
            Square({"width": 5}, 5)
            Square(5, {"height": 5})
            Square()
        with self.assertRaises(ValueError):
            Square(-1, 2)
            Square(1, -2)
            Square(0, 1)
            Square(1, 0)


if __name__ == "__main__":
    unittest.main()

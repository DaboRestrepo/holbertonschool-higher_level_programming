#!/usr/bin/python3
"""This module soport the TestBase class"""
import unittest
from unittest import result
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """This class test the Base class"""
    def nbObj(self):
        """Test the nb_objects"""
        Base._base__nb_objects = 0
        self.assertEqual(Base._base__nb_objects, 0)

    def Test_Init(self):
        """Test the initialize attribute"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(5)
        self.assertEqual(b2.id, 5)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b4 = Base("Hola")
        self.assertEqual(b4.id, "Hola")
        b5 = Base(4.5)
        self.assertEqual(b5.id, 4.5)
        b6 = Base([4, 5])
        self.assertEqual(b6.id, [4, 5])
        b7 = Base({"Hola": 5})
        self.assertEqual(b7.id, {"Hola": 5})

    def Test_to_json(self):
        """Test to json function"""
        dic1 = Rectangle(1, 2, 3, 4, 5)
        dic1_dictionary = dic1.to_dictionary()
        json_dictionary = Base.to_json_string([dic1_dictionary])
        self.assertEqual(json_dictionary, "{\"x\": 3, \"y\": 4, \"id\": 5,\
                                           \"height\": 2, \"width\": 1}")

    def Test_from_json(self):
        """Test from json function"""
        fj1 = Rectangle(1, 2, 3, 4)
        fj2 = Rectangle(5, 6, 7)
        result = Rectangle.save_to_file([fj1, fj2])
        self.assertEqual(result, "[{\"y\": 4, \"x\": 3, \"id\": 1,\
                                 \"width\": 1, \"height\": 2},\
                                 {\"y\": 0, \"x\": 7, \"id\": 2,\
                                 \"width\": 5, \"height\": 6}]")


if __name__ == '__main__':
    unittest.main()

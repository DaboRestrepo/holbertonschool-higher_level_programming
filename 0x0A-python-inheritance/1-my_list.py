#!/usr/bin/python3
"""This class sort and print a giving list
This supplies the print_sorted function"""


class MyList(list):

    def print_sorted(self):
        """This function sort and print a list"""
        print(sorted(self))

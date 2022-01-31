#!/usr/bin/python3
"""This class sort and print a giving list."""


class MyList(list):
    """Supplies the function print_sorted"""
    def print_sorted(self):
        """This function sort and print a list"""
        print(sorted(self))

#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MMMIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

#!/usr/bin/python3
"""This module make a list with the arguments"""


from sys import argv
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

list = []
file = 'add_item.json'
try:
    list = load_from_json_file(file)
except BaseException:
    pass
for i in range(1, len(argv)):
    list.append(argv[i])
save_to_json_file(list, file)

#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        new_list = [replace if item == search else item for item in my_list]
        return new_list

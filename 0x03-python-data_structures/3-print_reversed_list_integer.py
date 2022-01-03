#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        reverse_list = my_list[::-1]
        for i in range(len(reverse_list)):
            print('{:d}'.format(reverse_list[i]))

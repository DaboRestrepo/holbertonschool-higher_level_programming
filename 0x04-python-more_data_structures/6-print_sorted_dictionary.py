#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        for i in sorted(a_dictionary):
            print('{0} : {1}'.format(i, a_dictionary[i]))

#!/usr/bin/python3
from optparse import Values


def safe_print_list(my_list=[], x=0):
    if my_list is not None:
        count = 0
        for i in range(x):
            try:
                print(my_list[i], end="")
                count += 1
            except IndexError:
                break
        print()
        return count

#!/urs/bin/python3
from ast import Index
from typing import Type


def safe_print_list_integers(my_list=[], x=0):
    if my_list is not None:
        count = 0
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except (TypeError, ValueError):
                pass
    print()
    return count

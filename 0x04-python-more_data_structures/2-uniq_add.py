#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is not None:
        add = 0
        new_list = list(set(my_list))
        for item in range(len(new_list)):
            add += new_list[item]
        return add

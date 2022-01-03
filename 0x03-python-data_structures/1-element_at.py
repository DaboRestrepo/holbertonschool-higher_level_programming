#!/usr/bin/python3
def element_at(my_list, idx):
    if my_list[idx] > 0 | my_list[idx] < int(len(my_list)):
        return my_list[idx]
    else:
        return None

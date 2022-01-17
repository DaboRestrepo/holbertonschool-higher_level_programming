#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = 0
    new_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            new_list.append(div)
        except IndexError:
            div = 0
            new_list.append(div)
            print("out of range")
        except ZeroDivisionError:
            div = 0
            new_list.append(div)
            print("division by 0")
        except TypeError:
            div = 0
            new_list.append(div)
            print("wrong type")
    return new_list

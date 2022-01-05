#!/usr/bin/pytho3
def roman_to_int(roman_string):
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_list = list(roman_string)
    add = 0
    if type(roman_string) is not str or len(roman_string) == 0:
        return 0
    for i in roman_list:
        for j in dict:
            if i == j:
                add += dict[j]
    return add

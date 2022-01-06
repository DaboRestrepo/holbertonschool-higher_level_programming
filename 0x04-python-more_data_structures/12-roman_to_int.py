#!/usr/bin/pytho3
def roman_to_int(roman_string):
    if roman_string is not None and type(roman_string) == str:
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                'D': 500, 'M': 1000}
        add = 0
        roman = roman_string
        for i in range(len(roman)):
            if i < len(roman) - 1 and dict[roman[i]] < dict[roman[i + 1]]:
                add -= dict[roman[i]]
            else:
                add += dict[roman[i]]
        return add
    else:
        return 0

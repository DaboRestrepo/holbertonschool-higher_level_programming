#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    if n < 0:
        str2 = str
    elif n < len(str):
        str2 = str.replace(str[n], '')
    else:
        str2 = str
    return str2

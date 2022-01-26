#!/usr/bin/python3
"""
This is text_indentation module:

This supplies the text_indentation function.
"""


def text_indentation(text):
    """This function split the text depending of the delimiter:
    >>> text_indentation("Hola. mundo")
    Hola.
    mundo"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    end = 0
    init = 0
    for i in text:
        end += 1
        if i == '.' or i == '?' or i == ':':
            txt = text[init:end - 1] + i + "\n"
            print(txt)
            init = end + 1
    print(text[init:end], end="")

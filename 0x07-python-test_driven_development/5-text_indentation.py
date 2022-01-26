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
    list = []
    txt = text.replace(".", ".\n\n").replace(":", ":\n\n")\
              .replace("?", "?\n\n")
    list = [i.strip() for i in txt.split("\n")]
    for j in range(len(list)):
        if j == len(list) - 1:
            print(list[j], end="")
        else:
            print(list[j], end="\n")

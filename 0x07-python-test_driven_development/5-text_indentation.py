#!/usr/bin/python3
def text_indentation(text):
    end = 0
    init = 0
    for i in text:
        end += 1
        if i == '.' or i == '?' or i == ':':
            print(text[init:end], "\n")
            init = end + 1

#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is not None:
        length = len(sentence)
        first = sentence[0]
    else:
        length = len(sentence)
        first = 'None'
    return length, first,

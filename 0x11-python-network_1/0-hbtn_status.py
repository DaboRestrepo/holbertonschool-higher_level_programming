#!/usr/bin/python3
"""Fetch an URL with urllib."""
from urllib import request

if __name__ == "__main__":
    with request.urlopen('http://0.0.0.0:5050/status') as res:
        res_read = res.read()
        print('Body response:')
        print('\t- type: {}'.format(type(res_read)))
        print('\t- content: {}'.format(res_read))
        print('\t- utf8 content: {}'.format(res_read.decode('utf-8')))

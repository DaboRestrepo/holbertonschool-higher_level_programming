#!/usr/bin/python3
"""Fetch an URL with urllib."""
from email.headerregistry import ContentTypeHeader
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        res_read = res.read()
        print('Body response:')
        print('\t- type: {}'.format(type(res_read)))
        print('\t- content: {}'.format(res_read))
        print('\t- utf8 content: {}'.format(res.reason))

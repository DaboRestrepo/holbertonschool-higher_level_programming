#!/usr/bin/python3
"""Use request package to know the request status."""
import requests


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    status = r.text
    print('Body response:')
    print('\t- type: {}'.format(type(status)))
    print('\t- content: {}'.format(status))

#!/usr/bin/python3
"""Take a letter as parameter"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        data = {'q': argv[1]}
    else:
        data = {'q': ''}
    r = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        file = r.json()
        if file:
            print('[{}] {}'.format(file.get('id'), file.get('name')))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')

#!/usr/bin/python3
"""Post an email value to the URL request"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    values = {"email": argv[2]}
    data = parse.urlencode(values).encode('utf-8')
    with request.urlopen(url, data) as res:
        page = res.read().decode('utf-8')
        print(page)

#!/usr/bin/python3
"""Post an email value to the URL request"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}

    data = parse.urlencode(values)
    data = data.encode('ascii')
    r = request.Request(url, data)
    with request.urlopen(r) as res:
        page = res.read().decode('utf-8')

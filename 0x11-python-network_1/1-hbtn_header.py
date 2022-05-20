#!/usr/bin/python3
"""Request the request id."""
from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as res:
        header = res.headers
        print(header.get('X-Request-Id'))

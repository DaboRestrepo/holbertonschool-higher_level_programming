#!/usr/bin/python3
"""Get the Request Id value with request package."""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    header = r.headers
    print(header.get('X-Request-Id'))

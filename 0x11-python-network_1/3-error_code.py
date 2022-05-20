#!/usr/bin/python3
"""Display the body of the response and the error code if fails."""
from urllib import request, error
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        with request.urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))

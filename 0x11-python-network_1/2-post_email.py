#!/usr/bin/python3
"""Post an email value to the URL request"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    url_split = argv[1].split('/')
    if "post_email" in url_split:
        url = argv[1]
    else:
        url = argv[1] + "/post_email"
    values = {'email': argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    r = request.Request(url, data)
    with request.urlopen(r) as res:
        page = res.read().decode('utf-8')
        print(page)

#!/usr/bin/python3
"""Fetch an URL with urllib."""
from email.headerregistry import ContentTypeHeader
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
    res_read = res.read()
    print('Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'
          .format(type(res_read), res_read, res.reason))

#!/usr/bin/env python3
""" gtakes in a URL, sends a request to the URL
"""
from urllib import request, error
from sys import argv


url = argv[1]
req = request.Request(url)

try:
    # request.urlopen(req)
    with request.urlopen(req) as response:
        response = response.read()
        print(response.decode())
except error.HTTPError as eh:
    e = eh.read()
    print("Error code: ", eh.code)
except error.URLError as e:
    e = e.read()
    print(e.decode())

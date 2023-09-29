#!/usr/bin/python3
""" takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
"""
from urllib import request, parse
from sys import argv

url = argv[1]

with request.urlopen(url) as response:
    print(response.getheader('X-Request-Id'))

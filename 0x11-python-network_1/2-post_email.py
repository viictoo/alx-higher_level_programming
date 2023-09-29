#!/usr/bin/env python3
""" get last 10 commits from repo """
from urllib import request, parse
from sys import argv


url = argv[1]
email = argv[2]
values = {'email': email}
data = parse.urlencode(values)
data = data.encode('ascii')
req = request.Request(url, data)

with request.urlopen(req) as response:
    response = response.read()
    print(response.decode())

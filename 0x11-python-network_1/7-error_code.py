#!/usr/bin/env python3
""" get last 10 commits from repo """
import requests
from sys import argv


url = argv[1]

req = requests.get(url)

if req.status_code == requests.codes.ok:
    print(req.text)
else:
    print("Error code: ", req.status_code)

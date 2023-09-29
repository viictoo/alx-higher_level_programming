#!/usr/bin/env python3
""" get last 10 commits from repo """
import requests
from sys import argv


url = argv[1]

req = requests.get(url)
data = req.headers['X-Request-Id']

print(data)

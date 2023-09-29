#!/usr/bin/env python3
""" get last 10 commits from repo """
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


OWNER = argv[1]
PASSWORD = argv[2]
url = f"https://api.github.com/user"

req = requests.get(url, auth=HTTPBasicAuth(OWNER, PASSWORD))

data = req.json()
print(req.json().get('id'))
print(data)

#!/usr/bin/env python3
""" get last 10 commits from repo """
import requests
from sys import argv


url = argv[1]
email = argv[2]

req = requests.post(url, data={
        "email": email,
        })

data = req.text

print(data)

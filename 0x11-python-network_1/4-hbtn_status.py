#!/usr/bin/env python3
""" get last 10 commits from repo """
import requests


url = "https://alx-intranet.hbtn.io/status"

req = requests.get(url)

status = req.text
print("Body response:")
print("    - type: ", type(status))
print("    - content: ", status)

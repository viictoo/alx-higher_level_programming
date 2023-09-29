#!/usr/bin/python3
""" get last 10 commits from repo """
import requests
from sys import argv


url = "http://0.0.0.0:5000/search_user"
letter = ""

if len(argv) > 1:
    letter = argv[1]

req = requests.post(url, data={
    "q": letter
        })

res = req.json()
if res != {}:
    try:
        print(f"[{res['id']}] {res['name']}")
    except Exception:
        print("Not a valid JSON")
else:
    print("No result")

#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response
./7-error_code.py http://0.0.0.0:5000
 """
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        print(req.text)
    else:
        print(f"Error code: {req.status_code}")

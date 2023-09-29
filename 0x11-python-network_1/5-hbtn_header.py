#!/usr/bin/python3
""" takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
./5-hbtn_header.py https://alx-intranet.hbtn.io
 """
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    req = requests.get(url)
    print(req.headers.get('X-Request-Id'))

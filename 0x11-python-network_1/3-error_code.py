#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status
"""
from urllib import request, error
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            response = response.read()
            print(response.decode('utf-8'))
    except error.HTTPError as eh:
        print("Error code: ", eh.code)
    except error.URLError as e:
        e = e.read()
        print(e.decode())

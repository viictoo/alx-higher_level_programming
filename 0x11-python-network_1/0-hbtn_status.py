#!/usr/bin/python3
""""fetch status"""
from urllib import request


url = "https://alx-intranet.hbtn.io/status"
if __name__ == "__main__":
    with request.urlopen(url) as response:
        status = response.read()

        print("Body response:")
        print(f"\t- type: {type(status)}")
        print(f"\t- content: {status}")
        print(f"\t- utf8 content: {status.decode('utf-8')}")

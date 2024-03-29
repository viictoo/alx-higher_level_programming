#!/usr/bin/python3
""""fetch status"""
from urllib import request


url = "https://alx-intranet.hbtn.io/status"
if __name__ == "__main__":
    with request.urlopen(url) as response:
        response = response.read()
        print("Body response:")
        print(f"\t- type: {type(response)}")
        print(f"\t- content: {response}")
        print(f"\t- utf8 content: {response.decode('utf-8')}")

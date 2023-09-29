#!/usr/bin/python3
""" get last 10 commits from repo """
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    req = requests.get(url)
    status = req.text

    print("Body response:")
    print(f"\t- type: {type(status)}")
    print(f"\t- content: {status}")

#!/usr/bin/python3
""" fetch status """
from urllib import request


url = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    with request.urlopen(url) as response:
        status = response.read()

        print("Body response:")
        print("    - type: ", type(status))
        print("    - content: ", status)
        print("    - utf8 content: ", status.decode())

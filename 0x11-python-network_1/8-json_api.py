#!/usr/bin/python3
""" sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a """
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = ""
    if len(argv) > 1:
        letter = argv[1]

    req = requests.post(url, data={"q": letter})
    try:
        res = req.json()
        if res:
            try:
                if (res.get('id')) is None or (res.get('name')) is None:
                    print("Not a valid JSON")
                else:
                    print(f"[{res.get('id')}] {res.get('name')}")
            except ValueError:
                print("Not a valid JSON")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

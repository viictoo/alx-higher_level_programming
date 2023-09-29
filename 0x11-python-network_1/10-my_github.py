#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
    You must use Basic Authentication with a personal access token
    as password to access to your information
    (only read:user permission is needed)

./10-my_github.py papamuziko cisfun
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    OWNER = argv[1]
    PASSWORD = argv[2]
    url = f"https://api.github.com/user"

    req = requests.get(url, auth=HTTPBasicAuth(OWNER, PASSWORD))

    data = req.json()
    print(req.json().get('id'))
    print(data)

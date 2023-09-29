#!/usr/bin/python3
""" list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
./100-github_commits.py rails rails
"""
import requests
from sys import argv


if __name__ == "__main__":
    OWNER = argv[1]
    REPO = argv[2]
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/commits"
    req = requests.get(url)

    data = req.json()

    for key in data[0:10]:
        print("{}: {}".format(
                key.get('sha'),
                key.get('commit').get('author').get('name')))

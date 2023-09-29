#!/usr/bin/env python3
""" get last 10 commits from repo """
import requests
from sys import argv


OWNER = argv[1]
REPO = argv[2]
url = f"https://api.github.com/repos/{OWNER}/{REPO}/commits"

req = requests.get(url, headers={
        "Content-Type": "application/vnd.github+json", 
        "X-GitHub-Api-Version": "2022-11-28",
        })

data = req.json()

commits = []
for key in data:
    if 'commit' in key:
        commits.append(f"{key['sha']}: {key['commit']['author']['name']}")

for item in commits[-10:]:
    print(item)


#!/usr/bin/python3
""" takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response
./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    req = requests.post(url, data={
            "email": email})

    content = req.text

    print(content)

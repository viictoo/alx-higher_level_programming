#!/usr/bin/python3
"""  script that takes in a URL and an email,
    sends a POST request to the passed URL
    with the email as a parameter
./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    values = {'email': email}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(url, data)

    with request.urlopen(req) as response:
        response = response.read()
        print(response.decode('utf-8'))

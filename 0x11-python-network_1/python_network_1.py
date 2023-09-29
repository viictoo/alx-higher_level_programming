#!/usr/bin/python3
""" Doc
"""
from flask import Flask, Response, request, redirect, url_for
from flask import jsonify
import random, string
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'


@app.route('/post_email', methods=['POST'])
def post_email():
    return 'Your email is: {}'.format(request.form.get('email'))


@app.route('/status_404')
def status_404():
    return ('Error 404', 404)


@app.route('/status_401')
def status_401():
    return ('Error 401', 401)


@app.route('/status_500')
def status_500():
    return ('Error 500', 500)


def string_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join((random.choice(chars) for _ in range(size)))


@app.route('/search_user', methods=['POST'])
def search_user():
    data = {}
    q = request.form.get('q')
    if q is not None:
        if type(q) is str:
            if len(q) > 0:
                if ord(q[0]) in range(97, 123):
                    first_letter = q[0]
                    data['name'] = '{}{}'.format(q, string_generator(10, string.ascii_lowercase))
                    data['id'] = random.randrange(0, 10001, 2)
    res = jsonify(data)
    res.headers['Content-Type'] = 'application/json'
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

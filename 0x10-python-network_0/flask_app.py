#!/usr/bin/env python3
from flask import Flask, Response, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page'

@app.route('/route_1')
def route_1():
    return redirect(url_for('route_2'))

@app.route('/route_2')
def route_2():
    return 'Route 2'

@app.route('/route_3', methods=["GET", "PUT", "OPTIONS", "DELETE", "POST"])
def route_3():
    if request.method == 'DELETE':
        return "I'm a DELETE request"
    return "I'm not a DELETE request"

@app.route('/route_4', methods=['OPTIONS', 'HEAD', 'PUT'])
def route_4():
    res = Response('Did you GET it?')
    res.headers['Allow'] = 'OPTIONS, HEAD, PUT'
    return res

@app.route('/route_5')
def route_5():
    if request.headers.get('X-School-User-Id', '0') == '98':
        return 'Hello School!'
    return 'Who are you?'

@app.route('/route_6', methods=['POST'])
def route_6():
    get_params = [(k, request.args.get(k)) for k in request.args.keys()]
    post_params = [(k, request.form.get(k)) for k in request.form.keys()]
    result = []

    if get_params:
        result.append('GET params:')
        result.extend('\t{}: {}'.format(k, v) for k, v in get_params)

    if post_params:
        result.append('POST params:')
        result.extend('\t{}: {}'.format(k, v) for k, v in post_params)

    return '\n'.join(result)

@app.route('/catch_me', methods=['PUT'])
def catch_me_1():
    if request.method == 'PUT':
        return redirect(url_for('catch_me_2'), code=307)
    res = Response('No')
    res.headers['Allow'] = 'PUT'
    return res

@app.route('/catch_me_2', methods=['PUT'])
def catch_me_2():
    if request.form.get('user_id') == '98':
        return redirect(url_for('catch_me_3'), code=307)
    return 'You are not user_id = 98', 401

@app.route('/catch_me_3', methods=['PUT'])
def catch_me_3():
    if request.headers.get('Origin') == 'School':
        return 'You got me!'
    return 'You are not coming from School', 403

@app.route('/route_100')
def route_100():
    return 'Route 100', 289

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

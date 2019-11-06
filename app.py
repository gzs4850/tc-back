#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 14:47
# @Author  : z.g
from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def ping_pong():
    return jsonify("hello world")


if __name__ == '__main__':
    app.run(debug=True)
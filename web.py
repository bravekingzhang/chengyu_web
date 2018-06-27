# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/data')
def get_data():
    with open('data.json') as f:
        data = json.load(f)
    response = {
        "version": 100,
        "data": data
    }
    return jsonify(response), 200


@app.route('/version')
def check_version():
    response = {
        "version": 100
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)

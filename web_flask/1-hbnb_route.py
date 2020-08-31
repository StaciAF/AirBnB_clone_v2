#!/usr/bin/python3
"""
this script starts a Flask web app with 2 routes
listening on 0.0.0.0, port 5000
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def say_hello():
    return "Hello, HBNB"


@app.route("/hbnb", strict_slashes=False)
def web_HBNB():
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

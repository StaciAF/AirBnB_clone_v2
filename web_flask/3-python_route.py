#!/usr/bin/python3
"""
module notes, son
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def say_hello():
    """ function bound to route """
    return "Hello, HBNB"


@app.route("/hbnb", strict_slashes=False)
def web_HBNB():
    """ function bound to route """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def web_C_HBNB(text):
    """ function bound to route """
    return "C " + str(text).replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def web_py_HBNB(text="is cool"):
    """ function bound to route """
    return "Python " + str(text).replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

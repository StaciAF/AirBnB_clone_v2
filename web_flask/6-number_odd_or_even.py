#!/usr/bin/python3
"""
module notes, son
"""
from flask import Flask, render_template
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


@app.route("/number/<int:n>", strict_slashes=False)
def num_web_HBNB(n):
    """ function bound to route """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_temp_HBNB(n):
    """ function bound to route """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even_HBNB(n):
    """ function bound to route """
    if (n % 2) == 0:
        val = "even"
    else:
        val = "odd"
    return render_template('6-number_odd_or_even.html', n=n, value=val)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

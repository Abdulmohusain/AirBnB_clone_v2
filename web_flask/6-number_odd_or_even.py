#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Home page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb page"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_not_fun(text):
    """C is not fun page"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_awesome(text):
    """Python is really awesome. Unlike which is hard but we survived"""
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Number"""
    return "{} is a number".format(n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """Number"""
    if n % 2 == 0:
        odd_or_even = 'even'
    else:
        odd_or_even = 'odd'
    return render_template(
        "6-number_odd_or_even.html",
        num=n,
        odd_or_even=odd_or_even
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

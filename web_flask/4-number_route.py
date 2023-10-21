#!/usr/bin/python3
"""starts a Flask web application:"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """print hello hbnb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hhbnb():
    """print hello hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def namec(text):
    """print hello hbnb"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python/<text>", strict_slashes=False)
def namepython(text):
    """print hello hbnb"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False)
def namepython2():
    """print hello hbnb"""
    return "Python is cool"


@app.route("/number/<int:n>", strict_slashes=False)
def printNum(n):
    """print a number"""
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

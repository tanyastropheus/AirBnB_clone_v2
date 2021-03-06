#!/usr/bin/python3
from flask import Flask
import string
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
        return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
        return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
        return 'C %s' % text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text=None):
        if text:
                return 'Python %s' % text.replace('_', ' ')
        return 'Python is cool'


if __name__ == '__main__':
        # app.run() defaults to listening on port 5000
        app.run(host="0.0.0.0")

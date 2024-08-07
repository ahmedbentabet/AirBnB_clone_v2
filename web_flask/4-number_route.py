#!/usr/bin/python3
"""
This module contains a Flask web application with specific routes.
"""

from flask import Flask, abort

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' when accessing the root route."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB' when accessing the /hbnb route."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Display 'C ' followed by the value of the text variable.
    Replace underscore symbols with a space.
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    Display 'Python ' followed by the value of the text variable.
    Replace underscore symbols with a space.
    Default value of text is 'is cool'.
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<n>', strict_slashes=False)
def number_route(n):
    """
    Display 'n is a number' only if n is an integer.
    """
    try:
        n = int(n)
        return f"{n} is a number"
    except ValueError:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

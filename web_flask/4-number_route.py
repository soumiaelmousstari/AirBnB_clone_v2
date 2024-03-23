#!/usr/bin/python3
"""
4.Is it a number(a script that starts a Flask web application)
"""

from flask import Flask
application = Flask(__name__)


@application.route('/', strict_slashes=False)
def Hello_HBNB():
    """Her return is 'Hello_HBNB'"""
    return 'Hello HBNB!'


@application.route('/hbnb', strict_slashes=False)
def fun_HBNB():
    """Her return is 'HBNB'"""
    return 'HBNB'


@application.route('/c/<text>', strict_slashes=False)
def C_fun(text):
    """Her ruturn is 'C followd by text's value and replace('_', ' ')'"""
    return 'C ' + text.replace('_', ' ')


@application.route('/python/<text>', strict_slashes=False)
def Python_fun(text='is cool'):
    """Her return is 'Python followd by text's value and replace('_', ' ')'"""
    return 'Python ' + text.replace('_', ' ')


@application.route('/number/<n>', strict_slashes=False)
def isnumber_fun(n):
    """Her return 'n is a number if n is an integer'"""
    return '{:d} is a number'.format(n)


if __name__ == '__main__':
    application.run(host='0.0.0.0', port='5000')

#!/usr/bin/python3
"""
2.C is fun!(a script that starts a Flask web application)
"""
from flask import Flask
application = Flask(__name__)


@application.route('/', strict_slashes=False)
def Hello_HBNB():
    """Her return is 'Hello HBNB!'"""
    return 'Hello HBNB!'


@application.route('/hbnb', strict_slashes=False)
def fun_HBNB():
    """Her return is 'HBNB'"""
    return 'HBNB'


@application.route('/c/<text>', strict_slashes=False)
def c_fun(text):
    """
    Her return is 'C followed by the value of the
    text variable (replace underscore _ with a space)'
    """
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    application.run(host='0.0.0.0', port='5000')

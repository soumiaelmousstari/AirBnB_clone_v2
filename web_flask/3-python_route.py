#!/usr/bin/python3
"""
3.Python is cool!(a script that starts a Flask web applicatio)
"""
from flask import Flask
application = Flask(__name__)


@application.route('/', strict_slashes=False)
def Hello_HBNB():
    "Her return is 'Hello HBNB!'"
    return 'Hello HBNB!'


@application.route('/hbnb', strict_slashes=False)
def fun_HBNB():
    "Here return is 'HBNB'"
    return 'HBNB'


@application.route('/C/<text>', strict_slashes=False)
def C_fun(text):
    """
    Her return is 'C followed by the valye of the text variable
    replace(_ withe space)'
    """
    return 'C ' + text.raplace('_', ' ')


@application.route('/python/', strict_slashes=False)
@application.route('/python/<text>', strict_slashes=False)
def python_fun(text='is cool'):
    """
    Her return is 'Python followd by text's value(replace _ with space)'
    """
    return 'Python ' + text.replace('_', ' ')


if '__name__' == '__main__':
    application.run(host='0.0.0.0', port='5000')

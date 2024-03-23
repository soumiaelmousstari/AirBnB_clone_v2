#!/usr/bin/python3
"""
"""

from flask import Flask
application = Flask(__name__)


@application.route('/', strict_slashes=False)
def Hello_HBNB():
    """Her returns is 'Hello HBNB!'"""
    return 'Hello HBNB!'


@application.route('/hbnb', strict_slashes=False)
def fun_HBNB():
    """her return is 'HBNB'"""
    return 'HBNB'


if __name__ == '__main__':
    application.run(host='0.0.0.0', port='5000')

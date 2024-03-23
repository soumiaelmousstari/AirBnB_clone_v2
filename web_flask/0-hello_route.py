#!/usr/bin/python3
"""
0.Hello Flask!(a script that starts a Flask web application)
"""

from flask import Flask
application = Flask(__name__)


@application.route('/', strict_slashes=False)
def Hello_HBNB():
    """Her return is 'Hello HBNB!'"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    application.run(host='0.0.0.0', port='5000')

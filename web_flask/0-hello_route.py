#!/usr/bin/pyhton3
"""
0.Hello Flask!(a script that starts a Flask web application)
"""

from flask import Flask
application = Flask(__name__)

@application.route('/', strict_slashes=Flase)
def Hello_HBNB():
    return 'Hello HBNB!'

if __name__ == '__main__':
    application.run(host='0.0.0.0', port='5000')

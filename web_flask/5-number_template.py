#!/usr/bin/python3
"""
5.Number template(a script that starts a Flask web  application)
"""

from flask import Flask
application = Flask(__name__)


@application.route('/', strict_slashes=False)
def Hello_BHNB():
    """Her return is 'Hello HBNB'"""
    return 'Hello HBNB'


@application.route('/hbnb', strict_slashes=False)
def fun_HBNB():
    """Her return is 'HBNB'"""
    return 'HBNB'


@application.route('/C/<text>', strict_slashes=False)
def C_fun(text):
    """Her return is 'C + text.replace('_', ' ')'"""
    return 'C ' + text.replace('_', ' ')


@application.route('/python/<text>', strict_slashes=False)
def Python_fun(text='is cool'):
    """Her return is 'python + text.replace('_', ' ')'"""
    return 'Python ' + text.replace('_', ' ')


@application.route('/number/<int:n>', strict_slashes=False)
def isnumber_fun(n):
    """Her return n is number if n numebr"""
    return '{:d} is a number'.format(n)


@application.route('/number_template/<int:n>', strict_slashes=False)
def HTMLpage(n):
    """Her return is 'display HTML page if n is an integer'"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    application.run(host='0.0.0.0', port='5000')

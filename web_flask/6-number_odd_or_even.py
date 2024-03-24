#!/usr/bin/python3
"""
6.Odd or even?(a script that starts a Flask web application)
"""

from flask import Flask, render_template
application = Flask(__name__)


@application.route('/', strict_slashes=False)
def Hello_HBNB():
    """Her return is 'Hello HBNB!'"""
    return 'Hello HBNB!'


@application.route('/hbnb', strict_slashes=False)
def fun_HBNB():
    """Her return is 'HBNB'"""
    return 'HBNB'


@application.route('/C/<text>', strict_slashes=False)
def C_fun(text):
    """Her return is 'C + text.replace('_', ' ')'"""
    return 'C ' + text.replace('_', ' ')


@application.route('/python/<text>', strict_slashes=False)
def python_fun(text='is cool'):
    """Her return is 'Python followed by text.replace('_', ' ')'"""
    return 'Python ' + text.replace('_', ' ')


@application.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Her return is n is a number if n is an integer"""
    return '{:d} is a number'.format(n)


@application.route('/number_template/<int:n>', strict_slashes=False)
def HTML_page(n):
    """Display a HTML page if n is an integer"""
    return render_template('6-number_odd_or_even.html', m=n)


@application.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even_fun(n):
    """Display a HTML page is n is an integer"""
    var_text = 'odd'
    if n % 2 == 0:
        var_text = 'even'
    return render_template('6-number_odd_or_even.html', m=n, var_text=var_text)


if __name__ == '__main__':
    application.run(host='0.0.0.0', port='5000')

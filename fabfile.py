from fabric.api import *

def run():
    """ Run with Flask server. """
    local('python main.py')

def gunicorn():
    """ Run with Gunicorn server. """
    local('gunicorn -b 127.0.0.1:5000 main:app')

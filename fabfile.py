from fabric.api import *


def run():
    """ Run with Flask server. """
    local('python run.py')


def gunicorn():
    """ Run with Gunicorn server. """
    local('gunicorn run:app')


def shell():
    """ Start an interactive shell within application environment. """
    local('python shell.py')

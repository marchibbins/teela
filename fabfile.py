from fabric.api import *


def run():
    """ Run with Gunicorn server. """
    local('honcho start')


def dev():
    """ Run with Flask server. """
    local('honcho run python run.py')


def shell():
    """ Start an interactive shell within application environment. """
    local('honcho run python shell.py')


def test():
    """ Run tests. """
    local('honcho run python test.py')

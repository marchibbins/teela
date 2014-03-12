from fabric.api import *


def run():
    """ Run with Gunicorn server. """
    local('honcho start')


def dev():
    """ Run with Flask server. """
    local('honcho run python manage.py run')


def setup():
    """ Run with Flask server. """
    local('honcho run python manage.py setup')


def shell():
    """ Start an interactive shell within application environment. """
    local('honcho run python manage.py shell')


def test():
    """ Run tests. """
    local('honcho run python test.py')

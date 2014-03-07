from fabric.api import *

def run():
    """ Run with Flask server. """
    local('python main.py')

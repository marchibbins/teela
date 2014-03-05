from flask import Flask

def init():
    """ Create a Flask app. """
    app = Flask(__name__)

    return app

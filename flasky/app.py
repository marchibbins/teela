from config import Config
from flask import Flask

def init():
    """ Create a Flask app. """
    app = Flask(Config.PROJECT_NAME)
    configure_app(app)

    return app

def configure_app(app):
    """ Configure app with config object. """
    app.config.from_object(Config)

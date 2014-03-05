from config import Config
from extensions import cache
from flask import Flask
from frontend import frontend

def init():
    """ Create a Flask app. """
    app = Flask(Config.PROJECT_NAME)
    configure_app(app)
    configure_extensions(app)
    configure_blueprints(app)

    return app

def configure_app(app):
    """ Configure app with config object. """
    app.config.from_object(Config)

def configure_extensions(app):
    """ Configure Flask extensions """
    cache.init_app(app)

def configure_blueprints(app):
    """ Configure blueprints. """
    app.register_blueprint(frontend)

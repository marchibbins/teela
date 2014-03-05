from flask import Flask, render_template
from config import Config

from extensions import cache
from frontend import frontend

def init():
    """ Create a Flask app. """
    app = Flask(Config.PROJECT_NAME, template_folder=Config.TEMPLATE_FOLDER)

    configure_app(app)
    configure_extensions(app)
    configure_blueprints(app)
    configure_error_handlers(app)

    return app

def configure_app(app):
    """ Configure app with config object. """
    # http://flask.pocoo.org/docs/api/#configuration
    app.config.from_object(Config)

def configure_extensions(app):
    """ Configure Flask extensions. """
    # flask-cache
    cache.init_app(app)

def configure_blueprints(app):
    """ Configure blueprints. """
    app.register_blueprint(frontend)

def configure_error_handlers(app):
    """ Configure error templates. """
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template('errors/500.html'), 500

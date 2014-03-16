from flask import Blueprint, render_template, jsonify


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/')
def index():
    """ Create a JSON response. """
    return jsonify(status='success', message='Hello world')


@api.errorhandler(404)
def page_not_found(error):
    """ Custom 404 for this blueprint. Note: only handles exceptions
        raised by view functions, not missing routes under this url prefix. """
    # http://flask.pocoo.org/docs/api/#flask.Blueprint.errorhandler
    return jsonify(status='error', message='Not found'), 404

from flask import Blueprint, render_template, jsonify
from datetime import datetime

from teela.extensions import cache


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/')
@cache.cached(timeout=60)
def index():
    """ Create a JSON response. """
    return jsonify(status='success', time=datetime.now())


@api.errorhandler(404)
def page_not_found(error):
    """ Custom 404 for this blueprint. Note: only handles exceptions
        raised by view functions, not missing routes under this url prefix. """
    # http://flask.pocoo.org/docs/api/#flask.Blueprint.errorhandler
    return jsonify(status='error', description='Not found'), 404

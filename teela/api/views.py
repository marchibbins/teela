from flask import Blueprint, render_template, jsonify

api = Blueprint('api', __name__, url_prefix="/api")


@api.route('/')
def index():
    """ Create a JSON response. """
    return jsonify(status='success', message='Hello world')

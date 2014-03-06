from flask import Blueprint, render_template, jsonify

blueprint = Blueprint('api', __name__, url_prefix="/api")

@blueprint.route('/')
def index():
    return jsonify(status='success', message='Hello world')
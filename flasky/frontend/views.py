from flask import Blueprint

blueprint = Blueprint('frontend', __name__)

@blueprint.route('/')
def index():
    return "Hello World!"

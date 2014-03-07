from flask import Blueprint, render_template

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    """ Render a simple template. """
    return render_template('index.html')

from flask import Blueprint, render_template

from teela.frontend.models import Message


frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    """ Render a simple template. """
    message = Message.query.first()
    return render_template('frontend/index.html', message=message)

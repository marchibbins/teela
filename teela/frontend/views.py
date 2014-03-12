from flask import Blueprint, render_template
from models import Message

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    """ Render a simple template. """
    message = Message.query.first()

    return render_template('index.html', message=message)

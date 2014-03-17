from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired


class MessageForm(Form):

    """ Simple form to match Message model. """
    text = TextField(u'Text', [DataRequired()])

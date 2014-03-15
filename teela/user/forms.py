from flask.ext.wtf import Form
from wtforms import BooleanField, HiddenField, TextField, validators


class LoginForm(Form):

    """ """
    name = TextField(u'Name', [validators.Required()])
    remember = BooleanField('Remember me')
    next = HiddenField()

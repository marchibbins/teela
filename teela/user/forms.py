from flask.ext.wtf import Form
from wtforms import BooleanField, HiddenField, PasswordField, TextField
from wtforms.validators import DataRequired


class LoginForm(Form):

    """ """
    username = TextField(u'Username', [DataRequired()])
    password = PasswordField(u'Password', [DataRequired()])
    remember = BooleanField(u'Remember me')
    next = HiddenField()


class ReauthForm(Form):
    password = PasswordField(u'Password', [DataRequired()])
    next = HiddenField()

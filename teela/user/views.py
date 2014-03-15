from flask import Blueprint, request
from flask.ext.login import current_user, login_required, login_user, logout_user
from models import User

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/login')
def login():
    if current_user.is_authenticated():
        return 'Aready logged in'

    # form = LoginForm()
    next = request.args.get('next', None)

    if True:  # form.validate_on_submit():
        user = User.query.get(1)
        authenticated = True

        if user and authenticated:
            if login_user(user):
                # next
                return 'Log in success'
            else:
                return 'Log in fail'
        else:
            return 'Log in fail'

    return 'Login form'

@user.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out'

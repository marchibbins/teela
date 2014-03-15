from flask import Blueprint, request, redirect, render_template, url_for
from flask.ext.login import current_user, login_required, login_user, logout_user
from forms import LoginForm
from models import User


user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/login', methods=['GET', 'POST'])
def login():
    """ """
    if current_user.is_authenticated():
        return redirect(url_for('frontend.index'))

    form = LoginForm(next=request.args.get('next', None))

    if form.validate_on_submit():
        user, authenticated = User.authenticate(form.name.data)

        if user and authenticated:
            remember = request.form.get('remember') == 'y'
            if login_user(user, remember=remember):
                return redirect(form.next.data or url_for('frontend.index'))
            else:
                pass  # Login failed, e.g. inactive user
        else:
            pass  # Authentication failed, e.g. bad password

    return render_template('user/login.html', form=form)


@user.route('/logout')
@login_required
def logout():
    """ """
    logout_user()
    return redirect(url_for('frontend.index'))

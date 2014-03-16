from flask import Blueprint, request, redirect, render_template, url_for
from flask.ext.login import confirm_login, current_user, login_required, login_user, logout_user
from forms import LoginForm, ReauthForm
from models import User

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/login', methods=['GET', 'POST'])
def login():
    """ """
    if current_user.is_authenticated():
        return redirect(url_for('admin.index'))

    form = LoginForm(next=request.args.get('next'))

    if form.validate_on_submit():
        user, authenticated = User.authenticate(form.username.data,
                                                form.password.data)

        if user and authenticated:
            remember = request.form.get('remember') == 'y'
            if login_user(user, remember=remember):
                return redirect(form.next.data or url_for('admin.index'))
            else:
                form.non_field_errors = [u'Login failed']
        else:
            form.non_field_errors = [u'Usename and password incorrect']

    return render_template('user/login.html', form=form)


@user.route('/reauth', methods=['GET', 'POST'])
@login_required
def reauth():
    """ """
    form = ReauthForm(next=request.args.get('next'))

    if form.validate_on_submit():
        user, authenticated = User.authenticate(current_user.username,
                                                form.password.data)

        if user and authenticated:
            confirm_login()
            return redirect(form.next.data or url_for('admin.index'))
        else:
            form.non_field_errors = [u'Incorrect password']

    return render_template('user/reauth.html', form=form)


@user.route('/logout')
@login_required
def logout():
    """ """
    logout_user()
    return redirect(url_for('frontend.index'))

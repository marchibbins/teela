from flask import Blueprint

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/login')
def login():
    return 'Login'

from flask.ext.login import UserMixin
from sqlalchemy import Column
from teela.extensions import db
from werkzeug import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):

    """ """
    id = Column(db.Integer, primary_key=True)
    username = Column(db.String(64), nullable=False, unique=True)
    password_store = Column('password', db.String(64), nullable=False)

    def get_password(self):
        return self.password_store

    def set_password(self, password):
        self.password_store = generate_password_hash(password)

    def check_password(self, password):
        if self.password is None:
            return False

        return check_password_hash(self.password, password)

    password = db.synonym('password_store', descriptor=property(get_password, set_password))

    @classmethod
    def authenticate(self, username, password):
        """ """
        user = self.query.filter(User.username == username).first()

        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False

        return user, authenticated


def user_loader(id):
    """ """
    return User.query.get(id)

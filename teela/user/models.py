from flask.ext.login import UserMixin
from sqlalchemy import Column
from teela.extensions import db


class User(db.Model, UserMixin):

    """ """
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(64), nullable=False, unique=True)


def user_loader(id):
    return User.query.get(id)
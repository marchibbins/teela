from sqlalchemy import Column

from teela.extensions import db


class Message(db.Model):

    """ Simple model as an example. """
    id = Column(db.Integer, primary_key=True)
    text = Column(db.String(64))

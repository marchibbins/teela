from teela.extensions import db
from sqlalchemy import Column


class Message(db.Model):

    """ Simple model as an example. """
    id = Column(db.Integer, primary_key=True)
    text = Column(db.String(64))

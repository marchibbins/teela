from teela.extensions import db
from sqlalchemy import Column


class Message(db.Model):
    id = Column(db.Integer, primary_key=True)
    message = Column(db.String(64))

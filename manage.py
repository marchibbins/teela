from flask.ext.script import Manager, Shell

from teela import init
from teela.extensions import db
from teela.frontend import models

app = init()
manager = Manager(app)


@manager.command
def run():
    """ Run locally, host and port set by configuration. """
    app.run()


@manager.command
def setup():
    """ Init database and test message. """
    db.drop_all()
    db.create_all()

    # Example, otherwise required setup only
    message = models.Message(text=u'Hello World.')

    db.session.add(message)
    db.session.commit()


@manager.shell
def make_shell_context():
    """ Configure shell setup. """
    return dict(app=app, db=db, models=models)


if __name__ == "__main__":
    manager.run()

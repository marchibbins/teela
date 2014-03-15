from flask.ext.script import Manager, Shell

from teela import init
from teela.extensions import db
from teela.frontend import models as frontend_models
from teela.user import models as user_models

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
    message = frontend_models.Message(text=u'Hello World.')
    db.session.add(message)

    # Admin user
    admin = user_models.User(username=u'admin', password=u'password')
    db.session.add(admin)

    db.session.commit()


@manager.shell
def make_shell_context():
    """ Configure shell setup. """
    # http://flask-script.readthedocs.org/en/latest/#default-commands
    return dict(app=app, db=db)


if __name__ == "__main__":
    manager.run()

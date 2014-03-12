from flask.ext.script import Manager
from teela import init

app = init()
manager = Manager(app)


@manager.command
def run():
    """ Run locally, host and port set by configuration. """
    app.run()


if __name__ == "__main__":
    manager.run()

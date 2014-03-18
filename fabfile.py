from fabric.api import local, task


def honcho(command):
    """ Run Honcho command. """
    local('honcho %s' % command)


def honcho_run(command):
    """ Run a command using Honcho. """
    honcho('run %s' % command)


@task
def run():
    """ Run with Gunicorn server. """
    honcho('start')


@task
def dev():
    """ Run with Flask server. """
    honcho_run('python manage.py run')


@task
def setup():
    """ Set up application and database. """
    honcho_run('python manage.py setup')


@task
def shell():
    """ Start an interactive shell within application environment. """
    honcho_run('python manage.py shell')


@task
def test():
    """ Run tests. """
    honcho_run('python test.py')


@task
def clean():
    """ Delete pyc files. """
    local('find . -name \*.pyc -delete')

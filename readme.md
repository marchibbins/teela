# Teela

A [Flask](http://flask.pocoo.org/) bootstrap and application skeleton with [twelve-factor](http://www.12factor.net/) principles.

### Dependencies

- [Flask](http://flask.pocoo.org/) - Python Web framework
- [Flask-Cache](http://pythonhosted.org/Flask-Cache/) - Cache extension for Flask
- [Gunicorn](http://gunicorn.org/) - WSGI HTTP server
- [Honcho](https://github.com/nickstenning/honcho) - a Python clone of [Foreman](http://ddollar.github.com/foreman/)
- [Fabric](http://fabfile.org/) - command-line system admin, deployment, remote management

## Getting started

1. Install requirements (use [virtualenv](https://pypi.python.org/pypi/virtualenv))

        $ pip install -r requirements.txt

2. Run with Honcho

        $ honcho start

### Application and environment configuration

Honcho adds the contents of `.env` file as environment variables. The application boostrap configures Flask using these settings, so edit or add to this file as you please - see [Flask configuration](http://flask.pocoo.org/docs/config/).

**Note:** Defaults are defined in [the config class](teela/config.py) for some settings, so you don't need to duplicate these in your `.env` if you want to keep it minimal. Currently `SERVER_NAME` is the only requirement, which is used to determine the application `HOST` and `PORT`.

### Using procfiles

Honcho will use the main `Procfile` to run the application, which uses Gunicorn. Locally you can use `Procfile.dev` which runs Flask's development server. Set `DEBUG=True` in your `.env` file to auto-reload with code changes.

Specify a specific procile as follows:

    $ honcho start -f Procfile.dev

Really this file is just present as an example, you only need one procfile per environment.

#### See also:

- [The Twelve-Factor App](http://www.12factor.net/)
- [Declaring and Scaling Process Types with Procfile](https://devcenter.heroku.com/articles/procfile)
- [Dana](https://github.com/marchibbins/dana) - Twelve-Factor Django application

This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0)
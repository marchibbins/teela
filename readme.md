# Teela

A [Flask](http://flask.pocoo.org/) bootstrap and application skeleton with [twelve-factor](http://www.12factor.net/) principles.

### Dependencies

- [Flask](http://flask.pocoo.org/) - Python Web framework
- [Flask-Cache](http://pythonhosted.org/Flask-Cache/) - Cache extension for Flask
- [Gunicorn](http://gunicorn.org/) - WSGI HTTP server
- [Honcho](https://github.com/nickstenning/honcho) - a Python clone of [Foreman](http://ddollar.github.com/foreman/)
- [Fabric](http://fabfile.org/) - command-line system admin, deployment, remote management

### Getting started

1. Install requirements (use [virtualenv](https://pypi.python.org/pypi/virtualenv))

        $ pip install -r requirements.txt

2. Configure your application using the `.env` file

3. Run with Honcho

        $ honcho start

This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0)
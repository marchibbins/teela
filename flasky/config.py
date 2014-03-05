
class Config(object):
    """ """
    PROJECT_NAME = 'Flasky'

    ADMINS = [
        'marc@marchibbins.com'
    ]

    DEBUG = True

    # Flask-cache: http://pythonhosted.org/Flask-Cache/
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60

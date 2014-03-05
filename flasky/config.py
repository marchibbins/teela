
class Config(object):
    """ """
    PROJECT_NAME = 'Flasky'

    TEMPLATE_FOLDER = 'flasky/templates'

    ADMINS = [
        'marc@marchibbins.com'
    ]

    DEBUG = True

    # Flask-cache: http://pythonhosted.org/Flask-Cache/
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60


class Config(object):
    """ Basic object """
    PROJECT_NAME = 'Teela'

    TEMPLATE_FOLDER = 'teela/templates'

    ADMINS = [
        'marc@marchibbins.com'
    ]

    DEBUG = True

    # Flask-cache: http://pythonhosted.org/Flask-Cache/
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60

from os import environ


def env_var(key, default=None, required=False):
    """ Parse environment variable accordingly. """
    if required:
        # Throw KeyError for missing requirements
        val = environ[key]
    else:
        # Use default or None
        val = environ.get(key, default)

    # Replace booleans
    if val == 'True':
        val = True
    elif val == 'False':
        val = False

    return val


class Config(object):

    """ Configure application with envionment variables. """
    DEBUG = env_var('DEBUG', default=False)
    SERVER_NAME = env_var('SERVER_NAME', required=True)

    # Flask-cache: http://pythonhosted.org/Flask-Cache/
    CACHE_TYPE = env_var('CACHE_TYPE', default='simple')
    CACHE_DEFAULT_TIMEOUT = env_var('CACHE_DEFAULT_TIMEOUT', default=60)

from flask.ext.cache import Cache
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

cache = Cache()
db = SQLAlchemy()
login_manager = LoginManager()

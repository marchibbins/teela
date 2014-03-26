import os
import unittest

from teela import init
from teela import config


class AppTests(unittest.TestCase):

    """ Tests for application environment, config and bootstrap. """

    def setUp(self):
        """ Stores environment variables, which will be removed by tests and restored in tearDown. """
        self.environs = {
            'SERVER_NAME': os.environ['SERVER_NAME'],
            'SQLALCHEMY_DATABASE_URI': os.environ['SQLALCHEMY_DATABASE_URI'],
            'SECRET_KEY': os.environ['SECRET_KEY'],
        }

    def tearDown(self):
        """ Restores environment variables removed by tests. """
        os.environ['SERVER_NAME'] = self.environs['SERVER_NAME']
        os.environ['SQLALCHEMY_DATABASE_URI'] = self.environs['SQLALCHEMY_DATABASE_URI']
        os.environ['SECRET_KEY'] = self.environs['SECRET_KEY']

    def init_app(self):
        """ Reloads config module, attempts to init application. """
        reload(config)
        self.app = init()

    def test_server_name_requirement(self):
        """ Tests that KeyError is thrown when SERVER_NAME environ is not set. """
        del os.environ['SERVER_NAME']
        with self.assertRaises(KeyError):
            self.init_app()

    def test_db_uri_requirement(self):
        """ Tests that KeyError is thrown when SQLALCHEMY_DATABASE_URI environ is not set. """
        del os.environ['SQLALCHEMY_DATABASE_URI']
        with self.assertRaises(KeyError):
            self.init_app()

    def test_secret_key_requirement(self):
        """ Tests that KeyError is thrown when SECRET_KEY environ is not set. """
        del os.environ['SECRET_KEY']
        with self.assertRaises(KeyError):
            self.init_app()

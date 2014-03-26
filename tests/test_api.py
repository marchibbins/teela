import unittest

from teela import init


class ApiTests(unittest.TestCase):

    """ Tests for API. """

    def setUp(self):
        self.app = init().test_client()

    def test_index(self):
        """ Tests that API route returns 200 and JSON mimetype. """
        rv = self.app.get('/api/')
        self.assertTrue(rv.data)
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.mimetype, 'application/json')

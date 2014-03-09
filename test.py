from run import app
import unittest


class TestCase(unittest.TestCase):

    """ Base test case, common set up and tear down. """

    def setUp(self):
        self.app = app.test_client()


class AppTests(TestCase):

    """ Environment, config, bootstrap and static tests. """

    def test_favicon(self):
        rv = self.app.get('/static/favicon.ico')
        self.assertTrue(rv.data)
        self.assertEqual(rv.status_code, 200)
        rv.close()


class FrontendTests(TestCase):

    """ Tests for Frontend blueprint. """

    def test_index(self):
        rv = self.app.get('/')
        self.assertTrue(rv.data)
        self.assertEqual(rv.status_code, 200)

    def test_generic_404(self):
        rv = self.app.get('/404/')
        self.assertEqual(rv.status_code, 404)


class ApiTests(TestCase):

    """ Tests for API blueprint. """

    def test_index(self):
        rv = self.app.get('/api/')
        self.assertTrue(rv.data)
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.mimetype, 'application/json')


if __name__ == '__main__':
    unittest.main()

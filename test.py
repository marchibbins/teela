import unittest


def run():
    """ """
    suite = unittest.TestLoader().discover('tests')
    unittest.runner.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    run()

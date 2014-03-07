from teela import init

app = init()


def run():
    """ Run locally, host and port set by configuration. """
    app.run()

if __name__ == "__main__":
    run()

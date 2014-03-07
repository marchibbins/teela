from teela import init

app = init()

def run():
    """ Run locally. """
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    run()

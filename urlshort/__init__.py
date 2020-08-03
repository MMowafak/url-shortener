from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'h4r2t6o21p345213jwq'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app
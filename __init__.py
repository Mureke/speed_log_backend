from flask import Flask

from speed_tst.config import configure_app

from speed_tst.api.controllers import logs


def create_app(environment):
    app = Flask(__name__)

    configure_app(app)

    app.url_map.strict_slashes = False

    app.register_blueprint(logs, url_prefix='/api/logs')

    return app
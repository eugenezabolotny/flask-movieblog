from flask import Flask

from movieblog.config import run_config
from movieblog.api import movieblog_api


def run_app():
    app = Flask(__name__)
    app.config.from_object(run_config())
    app.register_blueprint(movieblog_api)

    return app

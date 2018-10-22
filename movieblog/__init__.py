from flask import Flask

from movieblog.config import run_config
from movieblog.api import movieblog_api
from movieblog.views import movieblog_views


def run_app():
    app = Flask(__name__)
    app.config.from_object(run_config())
    app.register_blueprint(movieblog_api)
    app.register_blueprint(movieblog_views)

    return app

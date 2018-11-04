from datetime import timedelta

from flask import Flask
from flask import render_template

from movieblog.config import run_config
from movieblog.api import movieblog_api
from movieblog.main import movieblog_views
from movieblog.db import db, ma


def page_not_found(e):
    return render_template('error404.html'), 404


def run_app():
    app = Flask(__name__)
    app.secret_key = 'super secret key'
    app.config.from_object(run_config())
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=1)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/movieblog'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    with app.app_context():
        db.init_app(app)
        db.create_all()
        db.session.commit()
        ma.init_app(app)
    app.register_blueprint(movieblog_api)
    app.register_blueprint(movieblog_views)
    app.register_error_handler(404, page_not_found)

    return app

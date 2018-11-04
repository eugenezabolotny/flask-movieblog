import json

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

with open('db/movieblog.json', 'r') as f:
    movieblog_data: dict = json.load(f)
    movies: list = movieblog_data['movies']
    news: list = movieblog_data['news']

users = {}

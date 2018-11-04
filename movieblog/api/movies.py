from flask import request
from flask.views import MethodView

from movieblog.db import db

from movieblog.main.schemas import movie_schema, movies_schema
from movieblog.main.models import MovieTable


class Movies(MethodView):

    @staticmethod
    def get(movie_id=None):

        if movie_id:
            movie: MovieTable = MovieTable.query.get(movie_id)

            if movie:
                return movie_schema.jsonify(movie)
            else:
                return 'no movie with such id'

        elif not movie_id:
            movies: list = MovieTable.query.order_by(MovieTable.id).all()
            return movies_schema.jsonify(movies)

    @staticmethod
    def post(movie_id=None):

        if movie_id:
            return 'method not allowed'

        elif not movie_id:
            data: dict = request.get_json()
            movie_keys = ['title', 'genre', 'year', 'duration', 'description', 'director', 'writers', 'stars']
            new_movie = {key: value for (key, value) in data.items() if key in movie_keys}

            if not MovieTable.query.filter_by(title=new_movie.get('title')).first():
                movie = MovieTable(**new_movie)
                db.session.add(movie)
                db.session.commit()
                return movie_schema.jsonify(new_movie)
            else:
                return 'movie with this title already exists'

    @staticmethod
    def put(movie_id=None):

        if movie_id:
            data: dict = request.get_json()
            movie: MovieTable = MovieTable.query.get(movie_id)

            if movie:
                for key in data.keys():
                    setattr(movie, key, data[key])
                db.session.commit()
                return movie_schema.jsonify(movie)
            else:
                return 'no movie with such id'

        elif not movie_id:
            return 'method not allowed'

    @staticmethod
    def delete(movie_id=None):

        if movie_id:
            movie: MovieTable = MovieTable.query.get(movie_id)
            if movie:
                db.session.delete(movie)
                db.session.commit()
                return 'movie deleted'
            else:
                return 'no movie with such id'

        elif not movie_id:
            return 'method not allowed'

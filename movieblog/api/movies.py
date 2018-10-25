from flask import Flask, request, jsonify
from flask.views import MethodView

from movieblog.db import movies

app = Flask(__name__)


class Movies(MethodView):

    def get(self):
        response: dict = movies
        return jsonify(response)

    def post(self):
        data: dict = request.get_json()
        movie_keys = ['title', 'genre', 'year', 'duration', 'description', 'director', 'writers', 'stars']
        new_movie = {key: value for (key, value) in data.items() if key in movie_keys}

        if not new_movie.get('title') in [movie['title'] for movie in movies]:
            new_movie['id'] = movies[-1]['id'] + 1 if movies else 1
            movies.append(new_movie)
            response = {'result': new_movie}
        else:
            response = {'result': False}

        return jsonify(response)


class Movie(MethodView):

    def get(self, movie_id):
        try:
            movie: dict = movies[movie_id]
        except IndexError:
            response = {'result': False}
        else:
            response = movie
        return jsonify(response)

    def put(self, movie_id):
        try:
            movie: dict = movies[movie_id]
        except IndexError:
            response = {'result': False}
        else:
            data: dict = request.get_json()
            for key in data.keys():
                if key in movie.keys():
                    movie[key] = data[key]
            response = movie

        return jsonify(response)

    def delete(self, movie_id):
        response = {'result': False}

        for movie in movies:
            if movie_id == movie['id']:
                movies.remove(movie)
                response = {'result': True}

        return jsonify(response)

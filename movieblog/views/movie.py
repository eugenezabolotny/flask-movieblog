from flask import render_template, jsonify
from flask.views import View, MethodView

from movieblog.db.data import movies


# class MovieView(View):
#     methods = ['GET']
#
#     def dispatch_request(self):
#         return render_template('movies.html', movies=movies)


class MovieView(MethodView):

    def get(self, movie_id):
        try:
            movie: dict = movies[movie_id]
        except IndexError:
            response = {'result': False}
        else:
            response = movie
        return render_template('movie.html', movie=response)

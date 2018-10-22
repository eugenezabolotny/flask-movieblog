from flask import render_template
from flask.views import View

from movieblog.db.data import movies


class MoviesView(View):
    methods = ['GET']

    def dispatch_request(self):
        return render_template('movies.html', movies=movies)

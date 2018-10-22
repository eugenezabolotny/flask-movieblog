from flask import render_template
from flask.views import View

from movieblog.db.data import news


class HomeView(View):
    methods = ['GET']

    def dispatch_request(self):
        return render_template('home.html', news=news)

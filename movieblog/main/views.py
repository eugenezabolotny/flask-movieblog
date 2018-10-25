from flask import render_template
from flask import Flask, session, redirect, url_for, request, flash
from flask.views import View, MethodView

from movieblog.db import movies
from movieblog.db import news
from movieblog.db import users
from .forms import RegisterForm
from .models import User


class HomeView(View):
    methods = ['GET']

    def dispatch_request(self):
        return render_template('home.html', news=news)


class MoviesView(View):
    methods = ['GET']

    def dispatch_request(self):
        return render_template('movies.html', movies=movies)


class MovieView(MethodView):

    def get(self, movie_id):
        try:
            movie: dict = movies[movie_id]
        except IndexError:
            response = {'result': False}
        else:
            response = movie
        return render_template('movie.html', movie=response)


class RegisterView(MethodView):

    def get(self):
        form = RegisterForm(request.form)
        return render_template('register.html', form=form)

    def post(self):
        form = RegisterForm(request.form)
        user = User(form.email.data, form.password.data, form.name.data, form.age.data)
        users[form.email.data] = user

        flash('You are now registered and can log in', 'success')
        return redirect(url_for('movieblog_views.home_view', news=news))

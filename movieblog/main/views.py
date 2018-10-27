from functools import wraps

from flask import render_template, session, redirect, url_for, request, flash, current_app
from flask.views import View, MethodView

from movieblog.db import movies
from movieblog.db import news
from movieblog.db import users
from .forms import RegisterForm
from .models import User


def requires_auth(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if not session.get('logged_in'):
            form = RegisterForm(request.form)
            flash('Authorization required', 'danger')
            return redirect(url_for('movieblog_views.login_view', form=form))
        return f(*args, **kwargs)

    return wrapped


class HomeView(View):
    methods = ['GET']

    def dispatch_request(self):
        return render_template('home.html', news=news)


class MoviesView(View):
    methods = ['GET', 'POST']

    @requires_auth
    def dispatch_request(self):
        return render_template('movies.html', movies=movies)


class MovieView(MethodView):

    @requires_auth
    def get(self, movie_id):
        try:
            movie: dict = movies[movie_id]
        except IndexError:
            response = {'result': False}
        else:
            response = movie
        return render_template('movie.html', movie=response)


def is_dev_mode():
    return current_app.config['MODE'] == 'DevConfig'


class RegisterView(MethodView):

    def get(self):
        form = RegisterForm(request.form)
        if is_dev_mode():
            flash(f"dev: {users if users else 'no registered users'}", 'warning')
        return render_template('register.html', form=form)

    def post(self):
        form = RegisterForm(request.form)
        user = User(form.email.data, form.password.data, form.name.data, form.age.data)
        users[form.email.data] = user

        flash('You are now registered and can log in', 'success')
        return redirect(url_for('movieblog_views.login_view', form=form))


class LoginView(MethodView):

    def get(self):
        form = RegisterForm(request.form)
        if is_dev_mode():
            flash(f"dev: {users if users else 'no registered users'}", 'warning')
        return render_template('login.html', form=form)

    def post(self):
        form = RegisterForm(request.form)
        email = request.form['email']
        password = request.form['password']

        if email in users.keys():
            if users[email].check_password(password):
                session.permanent = True
                session['logged_in'] = True
                session['user'] = vars(users[email])['name']
                flash('You are now logged in', 'success')
                return redirect(url_for('movieblog_views.home_view', news=news))
            else:
                flash(f'Wrong password for user {email}', 'danger')
                if is_dev_mode():
                    flash(f"dev: {users if users else 'no registered users'}", 'warning')
        else:
            flash(f'Username {email} not found', 'danger')
            if is_dev_mode():
                flash(f"dev: {users if users else 'no registered users'}", 'warning')

        return render_template('login.html', form=form)


class LogoutView(MethodView):
    def get(self):
        session.clear()
        flash(f'You are now logged out', 'success')
        return redirect(url_for('movieblog_views.home_view', news=news))

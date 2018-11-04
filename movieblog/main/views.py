from functools import wraps
from datetime import datetime

from flask import render_template, session, redirect, url_for, request, flash, current_app
from flask.views import View, MethodView
from werkzeug.security import check_password_hash

from movieblog.db import db
from movieblog.main.forms import RegisterForm
from movieblog.main.models import UserTable, MovieTable, NewsTable


def requires_auth(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if not session.get('logged_in'):
            flash('Authorization required', 'danger')
            return redirect(url_for('movieblog_views.login_view'))
        return f(*args, **kwargs)

    return wrapped


class HomeView(View):
    methods = ['GET']
    date_now = datetime.now()

    def dispatch_request(self):
        news = NewsTable.query.order_by(NewsTable.id).all()
        return render_template('home.html', news=news, date=self.date_now)


class MoviesView(View):
    methods = ['GET', 'POST']

    @requires_auth
    def dispatch_request(self):
        movies: list = MovieTable.query.order_by(MovieTable.id).all()
        return render_template('movies.html', movies=movies)


class MovieView(MethodView):

    @requires_auth
    def get(self, movie_id):
        movie: MovieTable = MovieTable.query.get(movie_id)
        return render_template('movie.html', movie=movie)


class RegisterView(MethodView):

    @staticmethod
    def get():
        form = RegisterForm(request.form)
        users = UserTable.query.order_by(UserTable.id).all()
        if current_app.config['MODE'] == 'DevConfig':
            flash("dev: {}".format(
                ', '.join([user.email for user in users]) if users else 'no registered users'
            ), 'warning')
        return render_template('register.html', form=form)

    @staticmethod
    def post():
        form = RegisterForm(request.form)
        user = UserTable(
            email=form.email.data,
            password=form.password.data,
            name=form.name.data,
            age=form.age.data
        )
        db.session.add(user)
        db.session.commit()
        flash('You are now registered and can log in', 'success')
        return redirect(url_for('movieblog_views.login_view'))


class LoginView(MethodView):

    @staticmethod
    def get():
        form = RegisterForm(request.form)
        users = UserTable.query.order_by(UserTable.id).all()
        if current_app.config['MODE'] == 'DevConfig':
            flash("dev: {}".format(
                ', '.join([user.email for user in users]) if users else 'no registered users'
            ), 'warning')
        return render_template('login.html', form=form)

    @staticmethod
    def post():
        form = RegisterForm(request.form)
        email = request.form['email']
        password = request.form['password']
        users = UserTable.query.order_by(UserTable.id).all()
        user = UserTable.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password_hash, password):
                session.permanent = True
                session['logged_in'] = True
                session['user'] = user.name
                flash('You are now logged in', 'success')
                return redirect(url_for('movieblog_views.home_view'))
            else:
                flash(f'Wrong password for user {user.email}: {user.password_hash}', 'danger')
                if current_app.config['MODE'] == 'DevConfig':
                    flash("dev: {}".format(
                        ', '.join([user.email for user in users]) if users else 'no registered users'
                    ), 'warning')
        else:
            flash(f'Username {user.email} not found', 'danger')
            if current_app.config['MODE'] == 'DevConfig':
                flash("dev: {}".format(
                    ', '.join([user.email for user in users]) if users else 'no registered users'
                ), 'warning')

        return render_template('login.html', form=form)


class LogoutView(MethodView):
    @staticmethod
    def get():
        session.clear()
        flash(f'You are now logged out', 'success')
        return redirect(url_for('movieblog_views.home_view'))

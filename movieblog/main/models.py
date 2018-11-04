from werkzeug.security import generate_password_hash

from movieblog.db import db


class UserTable(db.Model):
    __tablename__ = 'user_table'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(120))
    name = db.Column(db.String(120))
    age = db.Column(db.Integer)
    password_hash = db.Column(db.String(255))

    def __init__(self, email, password, name, age):
        self.email = email
        self.name = name
        self.age = age
        self.password_hash = generate_password_hash(password)


class MovieTable(db.Model):
    __tablename__ = 'movie_table'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(200))
    genre = db.Column(db.String(80))
    year = db.Column(db.String(4))
    duration = db.Column(db.String(40))
    description = db.Column(db.Text())
    director = db.Column(db.String(80))
    writers = db.Column(db.String(200))
    stars = db.Column(db.String(200))

    def __init__(self, title, genre, year, duration, description, director, writers, stars):
        self.title = title
        self.genre = genre
        self.year = year
        self.duration = duration
        self.description = description
        self.director = director
        self.writers = writers
        self.stars = stars


class NewsTable(db.Model):
    __tablename__ = 'news_table'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text())
    url = db.Column(db.String(2000))

    def __init__(self, title, description, url):
        self.title = title
        self.description = description
        self.url = url

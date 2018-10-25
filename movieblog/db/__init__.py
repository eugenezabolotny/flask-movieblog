import json

with open('db/movieblog.json', 'r') as f:
    movieblog_data: dict = json.load(f)
    movies: list = movieblog_data['movies']
    news: list = movieblog_data['news']

users = {}

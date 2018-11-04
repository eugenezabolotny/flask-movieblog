from flask import Blueprint

from .movies import Movies

movieblog_api = Blueprint('movieblog_api', __name__, static_folder='./static', template_folder='./template')

movieblog_api.add_url_rule('/api/movies', view_func=Movies.as_view('movies'))
movieblog_api.add_url_rule('/api/movies/<int:movie_id>', view_func=Movies.as_view('movie'))

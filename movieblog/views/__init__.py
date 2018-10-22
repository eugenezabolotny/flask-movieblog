from flask import Blueprint

from .home import HomeView
from .movies import MoviesView
from .movie import MovieView


movieblog_views = Blueprint('movieblog_views', __name__, static_folder='./static', template_folder='./template')

movieblog_views.add_url_rule('/', view_func=HomeView.as_view('home_view'))
movieblog_views.add_url_rule('/movies', view_func=MoviesView.as_view('movies_view'))
movieblog_views.add_url_rule('/movie/<int:movie_id>', view_func=MovieView.as_view('movie_view'))

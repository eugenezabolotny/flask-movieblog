from flask import Blueprint

from .views import HomeView, MoviesView, MovieView, RegisterView, LoginView, LogoutView


movieblog_views = Blueprint('movieblog_views', __name__, static_folder='./static', template_folder='./template')

movieblog_views.add_url_rule('/', view_func=HomeView.as_view('home_view'))
movieblog_views.add_url_rule('/movies', view_func=MoviesView.as_view('movies_view'))
movieblog_views.add_url_rule('/movie/<int:movie_id>', view_func=MovieView.as_view('movie_view'))
movieblog_views.add_url_rule('/register', view_func=RegisterView.as_view('register_view'))
movieblog_views.add_url_rule('/login', view_func=LoginView.as_view('login_view'))
movieblog_views.add_url_rule('/logout', view_func=LogoutView.as_view('logout_view'))

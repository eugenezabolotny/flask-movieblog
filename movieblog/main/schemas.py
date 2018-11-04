from movieblog.db import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('email', 'name', 'age', 'password_hash')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class MovieSchema(ma.Schema):
    class Meta:
        fields = ('title', 'genre', 'year', 'duration', 'description', 'director', 'writers', 'stars')


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


class NewsSchema(ma.Schema):
    class Meta:
        fields = ('title', 'description', 'url')


news_item_schema = NewsSchema()
news_schema = NewsSchema(many=True)

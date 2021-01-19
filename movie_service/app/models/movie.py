import datetime
from app import db


class Movie(db.Document):
    meta = {'collection': 'movie'}
    movie_id = db.StringField(max_length=50)
    movie_title = db.StringField(max_length=255)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.datetime.utcnow)
    launch_date = db.DateTimeField()
    genre = db.StringField(max_length=255)
    director = db.StringField(max_length=255)
    country = db.StringField(max_length=255)
    runtime = db.StringField(max_length=255)

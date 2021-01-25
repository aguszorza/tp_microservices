import datetime
from app import db


class Prices(db.Document):
    meta = {'collection': 'prices'}
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.datetime.utcnow)
    price = db.StringField(max_length=255)
    active = db.BooleanField(default=True)


class RentedMovies(db.Document):
    meta = {'collection': 'rented_movies'}
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.datetime.utcnow)
    movie_id = db.StringField(max_length=255)
    end_date = db.DateTimeField(default=datetime.datetime.utcnow)

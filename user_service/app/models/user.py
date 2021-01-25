import datetime
from app import db


class User(db.Document):
    meta = {'collection': 'user'}
    email = db.StringField(max_length=100, unique=True)
    id_auth = db.StringField(max_length=50)
    customer_name = db.StringField(max_length=50)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.datetime.utcnow)
    birthdate = db.DateTimeField()
    role = db.StringField(max_length=255)
    language = db.StringField(max_length=255, default="french")
    favorite_genres = db.ListField(db.StringField(), default=[])

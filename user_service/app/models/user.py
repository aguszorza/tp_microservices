from flask_security import UserMixin, RoleMixin
import datetime
from app import db


class User(db.Document, UserMixin):
    meta = {'collection': 'user'}
    id_auth = db.StringField(max_length=50)
    customer_name = db.StringField(max_length=50)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.datetime.utcnow)
    birthdate = db.DateTimeField()
    role = db.StringField(max_length=255)

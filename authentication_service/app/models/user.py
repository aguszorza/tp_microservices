from flask_security import UserMixin, RoleMixin
import datetime
from app import db


class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)


class User(db.Document, UserMixin):
    meta = {'collection': 'user'}
    id_customer = db.IntField()
    customer_name = db.StringField(max_length=50)
    email = db.StringField(max_length=100, unique=True)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.datetime.utcnow)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    fs_uniquifier = db.StringField(max_length=255)  # Necessary to invalidate tokens if password changes
    confirmed_at = db.DateTimeField()
    roles = db.ListField(db.ReferenceField(Role), default=[])

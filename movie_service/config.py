import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    MONGODB_SETTINGS = {
        'host': os.environ.get('MONGO_DATABASE_URL'),
    }


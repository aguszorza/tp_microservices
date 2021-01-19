import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    MONGODB_SETTINGS = {
        'host': os.environ.get('MONGO_DATABASE_URL'),
    }

    SECURITY_PASSWORD_HASH = os.environ.get("SECURITY_PASSWORD_HASH", 'bcrypt')
    SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT")
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    WTF_CSRF_ENABLED = False

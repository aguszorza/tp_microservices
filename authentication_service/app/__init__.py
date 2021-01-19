from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine

from flask_security import Security, MongoEngineUserDatastore


app = Flask(__name__)
app.config.from_object(Config)
db = MongoEngine(app)

from app.models.user import User, Role


user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)
# security = Security(app, user_datastore, register_form=ExtendedRegisterForm,
#                     confirm_register_form=ExtendedConfirmRegisterForm,
#                     register_blueprint=False)


from app import routes

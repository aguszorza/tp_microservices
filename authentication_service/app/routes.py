from app import app
from flask_security import auth_required, current_user
from flask import jsonify


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/verify_token')
@auth_required('session')
def verify_login():
    return jsonify({"id": str(current_user.id)}), 200


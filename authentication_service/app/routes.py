from app import app
from flask_security import auth_required, current_user
from flask import jsonify
from app.models.user import User


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/verify_token')
@auth_required('session')
def verify_login():
    return jsonify({"id": str(current_user.id)}), 200


@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.objects(id=user_id).first()
    if user is None:
        return 'error', 400
    user.delete()
    return '', 204


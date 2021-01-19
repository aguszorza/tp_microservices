from app import app
from flask import jsonify, request
import os
import requests
from app.models.user import User


AUTHENTICATION_URL = os.environ.get('AUTHENTICATION_URL')


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/user', methods=['POST'])  # TODO: verify it is loged in and is admin
def register_user():
    output = requests.post(f"{AUTHENTICATION_URL}register", json=request.json)
    if output.status_code >= 300:
        return output.json(), 400
    user = User()
    user.birthdate = request.json.get('birthdate')
    user.customer_name = request.json.get('customer_name')
    user.role = request.json.get('role')
    user.id_auth = output.json()["response"]["user"]["id"]
    user.save()
    return output.json(), output.status_code


@app.route('/user', methods=['GET'])
def get_user():
    output = requests.get(f"{AUTHENTICATION_URL}verify_token", cookies={'session': request.cookies.get('session')})  # TODO: put it as annotation
    if output.status_code >= 300:
        return output.json(), output.status_code
    user = User.objects(id_auth=output.json()["id"]).first()
    return user.to_json(), output.status_code


@app.route('/user/<user_id>', methods=['GET'])
def get_user_from_id(user_id):
    output = requests.get(f"{AUTHENTICATION_URL}verify_token", cookies={'session': request.cookies.get('session')})  # TODO: put it as annotation
    if output.status_code >= 300:
        return output.json(), output.status_code
    id = output.json()["id"]
    if id != user_id:
        user = User.objects(id_auth=id).first()
        if user is None or user.role != 'admin':
            return "error", 401
    user = User.objects(id_auth=user_id).first()
    return user.to_json(), output.status_code


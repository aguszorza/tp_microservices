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
    user.email = request.json.get('email')
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


@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    output = requests.get(f"{AUTHENTICATION_URL}verify_token", cookies={'session': request.cookies.get('session')})  # TODO: put it as annotation
    if output.status_code >= 300:
        return output.json(), output.status_code
    id = output.json()["id"]
    admin_user = User.objects(id_auth=id).first()
    if admin_user is None or admin_user.role != 'admin':
        return "error", 401
    user = User.objects(id_auth=user_id).first()
    user.update(birthdate=request.json.get('birthdate', user.birthdate), customer_name=request.json.get('customer_name', user.customer_name))
    user.reload()
    return user.to_json(), 200


@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    output = requests.get(f"{AUTHENTICATION_URL}verify_token", cookies={'session': request.cookies.get('session')})  # TODO: put it as annotation
    if output.status_code >= 300:
        return output.json(), output.status_code
    id = output.json()["id"]
    admin_user = User.objects(id_auth=id).first()
    if admin_user is None or admin_user.role != 'admin':
        return "error", 401
    output = requests.delete(f"{AUTHENTICATION_URL}user/{user_id}")
    if output.status_code >= 300:
        return '', 400
    user = User.objects(id_auth=user_id).first()
    user.delete()
    return '', 204


@app.route('/user/<user_id>/rights', methods=['PUT'])
def update_user_rights(user_id):
    output = requests.get(f"{AUTHENTICATION_URL}verify_token", cookies={'session': request.cookies.get('session')})  # TODO: put it as annotation
    if output.status_code >= 300:
        return output.json(), output.status_code
    id = output.json()["id"]
    admin_user = User.objects(id_auth=id).first()
    if admin_user is None or admin_user.role != 'admin':
        return "error", 401
    user = User.objects(id_auth=user_id).first()
    user.update(role=request.json.get('role', user.role))
    user.reload()
    return user.to_json(), 200


@app.route('/user/<user_id>/preference', methods=['PUT'])
def update_user_preference(user_id):
    output = requests.get(f"{AUTHENTICATION_URL}verify_token", cookies={'session': request.cookies.get('session')})  # TODO: put it as annotation
    if output.status_code >= 300:
        return output.json(), output.status_code
    id = output.json()["id"]
    if id != user_id:
        return "error", 401
    user = User.objects(id_auth=user_id).first()
    data = {
        "language": request.json.get('language', user.language),
        "favorite_genres": request.json.get('favorite_genres', user.favorite_genres)
    }
    user.update(**data)
    user.reload()
    return user.to_json(), 200


@app.route('/user/<user_id>/preference', methods=['GET'])
def get_user_preference(user_id):
    output = requests.get(f"{AUTHENTICATION_URL}verify_token", cookies={'session': request.cookies.get('session')})  # TODO: put it as annotation
    if output.status_code >= 300:
        return output.json(), output.status_code
    id = output.json()["id"]
    if id != user_id:
        return "error", 401
    user = User.objects(id_auth=user_id).first()
    return jsonify({"language": user.language, "favorite_genres": user.favorite_genres}), 200


@app.route('/user/movie/<movie_id>/history', methods=['POST'])
def add_movie(movie_id):
    output = requests.get(f"{AUTHENTICATION_URL}verify_token", cookies={'session': request.cookies.get('session')})  # TODO: put it as annotation
    if output.status_code >= 300:
        return output.json(), output.status_code
    id = output.json()["id"]
    user = User.objects(id_auth=id).first()
    user.update(push__watched_movies=movie_id)
    return "", 204


@app.route('/user/<user_id>/movie/history', methods=['GET'])
def get_movie_history(user_id):
    output = requests.get(f"{AUTHENTICATION_URL}verify_token", cookies={'session': request.cookies.get('session')})  # TODO: put it as annotation
    if output.status_code >= 300:
        return output.json(), output.status_code
    id = output.json()["id"]
    if id != user_id:
        return "error", 401
    user = User.objects(id_auth=user_id).first()
    return jsonify({"watched_movies": user.watched_movies}), 200


@app.route('/user/movie/<movie_id>', methods=['POST'])
def add_movie_to_my_list(movie_id):
    output = requests.get(f"{AUTHENTICATION_URL}verify_token", cookies={'session': request.cookies.get('session')})  # TODO: put it as annotation
    if output.status_code >= 300:
        return output.json(), output.status_code
    id = output.json()["id"]
    user = User.objects(id_auth=id).first()
    user.update(push__my_list=movie_id)
    return "", 204


@app.route('/user/<user_id>/movie', methods=['GET'])
def get_my_movie_list(user_id):
    output = requests.get(f"{AUTHENTICATION_URL}verify_token", cookies={'session': request.cookies.get('session')})  # TODO: put it as annotation
    if output.status_code >= 300:
        return output.json(), output.status_code
    id = output.json()["id"]
    if id != user_id:
        return "error", 401
    user = User.objects(id_auth=user_id).first()
    return jsonify({"my_list": user.my_list}), 200

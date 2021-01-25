from app import app
from functools import wraps
from flask import jsonify, request, abort
import os
import requests

from app.models.movie import Movie


USER_URL = os.environ.get('USER_URL')


def validate_admin_role(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        output = requests.get(f"{USER_URL}user", cookies={'session': request.cookies.get('session')})  # TODO: put it as annotation
        if output.status_code >= 300:
            return abort(403)
        if output.json()["role"] != "admin":
            return abort(403)

        return function(*args, **kwargs)
    return decorated_function


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/movie', methods=['GET'])
def get_movie():
    movies = Movie.objects().all()
    return jsonify(movies), 200


@app.route('/movie', methods=['POST'])
@validate_admin_role
def post_movie():
    movie = Movie()
    movie.runtime = request.json.get('runtime')
    movie.director = request.json.get('director')
    movie.country = request.json.get('country')
    movie.genre = request.json.get('genre')
    movie.launch_date = request.json.get('launch_date')
    movie.movie_title = request.json.get('movie_title')
    movie.save()
    return movie.to_json(), 200


@app.route('/movie/<movie_id>', methods=['GET'])
def get_movie_from_id(movie_id):
    movie = Movie.objects(id=movie_id).first()
    return movie.to_json(), 200


@app.route('/movie/<movie_id>', methods=['PUT'])
@validate_admin_role
def update_movie(movie_id):
    movie = Movie.objects(id=movie_id).first()
    movie.update(**request.json)
    movie.reload()
    return movie.to_json(), 200


@app.route('/movie/<movie_id>', methods=['DELETE'])
@validate_admin_role
def delete_movie(movie_id):
    movie = Movie.objects(id=movie_id).first()
    movie.delete()
    return '', 204


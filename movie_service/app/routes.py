from app import app
from flask import jsonify, request
import os
import requests

from app.models.movie import Movie


AUTHENTICATION_URL = os.environ.get('AUTHENTICATION_URL')


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/movie', methods=['GET'])
def get_movie():
    movies = Movie.objects().all()
    return jsonify(movies), 200

@app.route('/movie', methods=['POST'])
def post_movie():
    # verify user
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
def update_movie(movie_id):
    output = requests.get(f"{AUTHENTICATION_URL}verify_token", cookies={'session': request.cookies.get('session')})  # TODO: put it as annotation
    if output.status_code >= 300:
        return output.json(), output.status_code
    id = output.json()["id"]
    admin_user = User.objects(id_auth=id).first()
    if admin_user is None or admin_user.role != 'admin':
        return "error", 401
    movie = Movie.objects(id=movie_id).first()
    movie.update(**request.json)
    movie.reload()
    return user.to_json(), 200
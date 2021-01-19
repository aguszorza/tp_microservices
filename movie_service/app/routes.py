from app import app
from flask import jsonify, request
import os
import requests


AUTHENTICATION_URL = os.environ.get('AUTHENTICATION_URL')


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/movie', methods=['GET'])
def get_movie():
    output = requests.get()
    if output.status_code >= 300:
        return output.json(), output.status_code
    movie = Movie.objects(id_movie=output.json()["id"]).first()
    return movie.to_json(), output.status_code

@app.route('/movie', methods=['POST'])
def post_movie():
    output = requests.post(f"{AUTHENTICATION_URL}register", json=request.json)
    if output.status_code >= 300:
        return output.json(), 400
    movie = Movie()
    movie.runtime = request.json.get('runtime')
    movie.director = request.json.get('director')
    movie.country = request.json.get('country')
    movie.genre = request.json.get('genre')
    movie.launch_date = request.json.get('launch_date')
    movie.movie_title = request.json.get('movie_title')
    movie.movie_id = output.json()["response"]["movie"]["id"]
    movie.save()
    return output.json(), output.status_code

@app.route('/movie/<movie_id>', methods=['GET'])
def get_user_from_id(movie_id):
    output = requests.get()
    if output.status_code >= 300:
        return output.json(), output.status_code
    id = output.json()["id"]
    if id != movie_id:
        movie = Movie.objects(movie_id=id).first()
        if movie is None or movie.role != 'admin':
            return "error", 401
    movie = Movie.objects(movie_id=movie_id).first()
    return movie.to_json(), output.status_code

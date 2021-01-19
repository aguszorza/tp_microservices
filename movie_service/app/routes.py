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

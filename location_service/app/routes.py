from app import app
from flask import request, abort, jsonify
import os
import requests
import datetime

from app.models.location import Prices, RentedMovies


USER_URL = os.environ.get('USER_URL')
MOVIE_URL = os.environ.get('MOVIE_URL')


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/rent/price', methods=['PUT'])
def save_price():
    old_price = Prices.objects(active=True).first()
    if old_price is not None:
        old_price.active = False
        old_price.save()
    price = Prices()
    price.price = request.json.get('price')
    price.save()
    return "", 204


@app.route('/movie/<movie_id>/rent', methods=['POST'])
def rent_movie(movie_id):
    output = requests.get(f"{USER_URL}user", cookies={'session': request.cookies.get('session')})  # TODO: put it as annotation
    if output.status_code >= 300:
        return abort(403)
    output = requests.get(f"{MOVIE_URL}movie/{movie_id}")  # TODO: put it as annotation
    if output.status_code >= 300:
        return abort(404)
    rented_movie = RentedMovies()
    rented_movie.movie_id = movie_id
    rented_movie.end_date = request.json.get("end_date")
    rented_movie.save()
    return "", 204


@app.route('/movie/rent', methods=['GET'])
def get_rented_movies():
    rented_movies = RentedMovies.objects(end_date__gt=datetime.datetime.now()).all()
    print(rented_movies)
    return jsonify(rented_movies), 200

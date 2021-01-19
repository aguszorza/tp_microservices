from app import app
from flask import jsonify, request
import os
import requests


AUTHENTICATION_URL = os.environ.get('AUTHENTICATION_URL')


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/user', methods=['GET'])
def get_user():
    output = requests.get(f"{AUTHENTICATION_URL}verify_token", cookies={'session': request.cookies.get('session')})  # TODO: put it as annotation
    return output.json(), output.status_code


from config.app import app,socketio,migrate
from config.ma import ma
from config.db import db
from route.api import api
import resources.jwt
from time import time
from flask import jsonify
from uuid import uuid4


@app.before_first_request
def before_first_request():
    db.create_all()













if __name__ == "__main__":

    db.init_app(app)
    ma.init_app(app)

    socketio.run(app,port=5000,debug=True)
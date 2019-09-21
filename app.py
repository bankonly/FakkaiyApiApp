from config.app import socketio,migrate
from config.ma import ma
from config.db import db

from route.api import api
from route.web import app
import resources.jwt
from flask import jsonify
from uuid import uuid4
from datetime import date,datetime


def run():
    print(datetime.now())
    print('5')

# schedule.add_job(run,'cron',second='2')

if __name__ == "__main__":

    db.init_app(app)
    ma.init_app(app)

    socketio.run(app,port=5000,debug=True)
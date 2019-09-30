import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import migrate
from dotenv import load_dotenv
from flask_restful import Api
from flask_jwt_extended import *
from flask_socketio import SocketIO
from flask_marshmallow import Marshmallow
from uuid import uuid4
from helper.handleexception import HandleExcetion

app = Flask(__name__)

# cors origin allow
CORS(app)

# file allow
ALLOWED_TYPE = {'txt','jpg','png','jpeg','gif'}

# load env file
load_dotenv('.env')
app.config['UPLOAD_FOLDER'] = os.environ.get('IMG_UPLOAD_PATH')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access','refresh']


api = Api(app)
jwt = JWTManager(app)
socketio = SocketIO(app,cors_allowed_origins='*')


@app.errorhandler(TypeError)
def errorhandler(error):
    return HandleExcetion.output(error),500

@app.errorhandler(AttributeError)    
def errorhandler(error):
    return HandleExcetion.output(error),500

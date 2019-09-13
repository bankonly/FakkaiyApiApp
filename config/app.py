import os



from flask import Flask
from flask_cors import CORS
from flask_migrate import migrate
from dotenv import load_dotenv
from flask_restful import Api
from flask_jwt_extended import *
from flask_socketio import SocketIO
from flask_marshmallow import Marshmallow



app = Flask(__name__)

# cors origin allow
CORS(app)

# load env file
load_dotenv('.env')

print('___________')
print(os.environ.get('DATABASE_URI'))
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access','refresh']


api = Api(app)
jwt = JWTManager(app)
socketio = SocketIO(app)




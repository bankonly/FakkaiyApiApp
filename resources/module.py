from flask_restful import Resource,reqparse
from config.strings import gettex
from flask import request as req,jsonify
from time import time
from uuid import uuid4
from config.db import db
from werkzeug.security import safe_str_cmp
from config.app import jwt_required,get_jwt_claims
from middleware.isAdmin import IsAdminMiddleware
from middleware.user import UserMiddleware
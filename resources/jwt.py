from config.app import jwt
from flask import request
from schema.user import UserSchema
@jwt.user_claims_loader
def user_claims_loader(user_claims):
    return user_claims

@jwt.token_in_blacklist_loader
def token_in_blacklist_loader(identity):
    pass
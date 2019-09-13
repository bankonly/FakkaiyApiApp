from schema.user import UserModel,UserSchema
from resources.module import (
    req,gettex,Resource,reqparse,safe_str_cmp
)
from config.app import create_access_token,create_refresh_token

parser = reqparse.RequestParser()
parser.add_argument('email',required=True)
parser.add_argument('password',required=True)

class Authenticate(Resource):
    @classmethod
    def post(cls):
        value = parser.parse_args()
        user = UserModel.findByEmail(value.email)
        if user and safe_str_cmp(user.password,value.password):
            return cls.newToken(user)
        
        return gettex('NOT_FOUND'),400

    @classmethod
    def newToken(self,user):
        access_token = create_access_token(identity=user.userId,user_claims=UserSchema().dump(user),fresh=True)
        refresh_token = create_refresh_token(user.userId)
        return {
            'access_token':f'Bearer {access_token}',
            'refresh_token':refresh_token
        },201

        

from resources.module import (
    gettex,req,Resource,jwt_required,get_jwt_claims,time,reqparse
)
from schema.profile import ProfileModel,ProfileSchema

parser = reqparse.RequestParser()
parser.add_argument('lastname',required=True)
parser.add_argument('facebook',required=True)
parser.add_argument('instragram',required=True)
parser.add_argument('location',required=True)
parser.add_argument('avatar',required=True)

class ProfileResource(Resource):
    @jwt_required 
    def get(self):
        
        data = get_jwt_claims()
        profile = ProfileModel.findById(data['userId'])
        return ProfileSchema().dump(profile)
    
    @jwt_required
    def post(self):

        value = parser.parse_args()
        data = get_jwt_claims()

        value.update({'userId':data['userId']})
        profile = ProfileModel.findById(data['userId'])
        if profile is not None:
            profile.lastname = value.lastname
            profile.facebook = value.facebook
            profile.instragram = value.instragram
            profile.location = value.location
            profile.avatar = value.avatar
            profile.insert()
            return ProfileSchema().dump(profile)
            
        profile = ProfileSchema().load(value)
        profile.insert()
        return ProfileSchema().dump(profile)
        

            




        

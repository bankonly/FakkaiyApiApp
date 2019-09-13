from schema.user import UserSchema,UserModel
from resources.module import (
    db,req,Resource,uuid4,time,gettex,jwt_required,get_jwt_claims
)


class UserResource(Resource):

    @classmethod
    @jwt_required
    def get(cls):
        # return get_jwt_claims()
        user = UserModel.fetchAll()
        return UserSchema(many=True).dump(user)

    def post(self):
        value = req.get_json()
        user = UserSchema().load(value,session=db.session)
        isEmail = UserModel.findByEmail(user.email)
        isName = UserModel.findByName(user.name)
        if isEmail is not None or isName is not None:
            return gettex('EXIST'),400
        try:
            user.insert()
        except:
            return gettex('SOMETHING_WRONG'),500
    
        return UserSchema().dump(user)

    @jwt_required
    def put(self):
        userid = get_jwt_claims()['userId']
        value = req.get_json()
        user = UserModel.findById(userid)
        if user is None:
            return gettex('NOT_FOUND'),400
        user.name = value['name']
        user.insert()
        return UserSchema().dump(user)

class InheritUserResource(UserResource):

    @jwt_required
    def get(self,userid):
        user = UserModel.findById(userid)
        if user is None:
            return gettex('NOT_FOUND'),400

        return UserSchema().dump(user)

    @jwt_required
    def delete(self,userid):
        user = UserModel.findById(userid)
        if user is None:
            return gettex('NOT_FOUND'),400
        try:
            user.delete()
        except:
            return gettex('SOMETHING_WRONG'),500
            
        return UserSchema().dump(user)

    def put(self,userid):
        pass





from schema.user import UserSchema,UserModel
from resources.module import (
    db,req,Resource,uuid4,time,gettex,jwt_required,get_jwt_claims
)


class UserResource(Resource):

    @classmethod
    @jwt_required
    def get(cls):
      
        user = UserModel.fetchAll()
        alluser = UserSchema(many=True).dump(user)
        return {
            'data': alluser[0]
        }

    def post(self):
        value = req.get_json()
        value.update({'userId':uuid4().hex})
        user = UserSchema().load(value,session=db.session)
        isEmail = bool(UserModel.findByEmail(user.email))
        isName = bool(UserModel.findByName(user.name))
        
        if isEmail or isName:
            return gettex('EXIST'),422
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
        if not bool(user):
            return gettex('NOT_FOUND'),400
            
        try:
            user.name = value['name']
            user.insert()
        except:
            return gettex('SOMETHING_WRONG'),500

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

    @classmethod
    def put(self,userid):
        pass





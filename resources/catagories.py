from schema.catagories import CatagoryModel,CatagorySchema
from resources.module import (
    Resource,reqparse,gettex,IsAdminMiddleware,db,uuid4
)

parser = reqparse.RequestParser()
parser.add_argument('catName',required=True)

class CatagoryResource(Resource):
      
    @IsAdminMiddleware.PermissionMiddleware
    def get(self):
        data = CatagoryModel.fetchAll()
        return CatagorySchema(many=True).dump(data),200

    @IsAdminMiddleware.PermissionMiddleware
    def post(self):
        dataBody = parser.parse_args()
        dataBody.update({'catId':uuid4().hex})
        cat = CatagorySchema().load(dataBody,session=db.session)
        isExist = bool(CatagoryModel.findByName(dataBody.catName))

        if isExist:
            return gettex('EXIST'),422
        try:
            cat.insert()
        except:
            return gettex('SOMETHING_WRONG'),500

        return CatagorySchema().dump(cat)

class AbsCatagoryResource(Resource):

    @IsAdminMiddleware.PermissionMiddleware
    def get(self,catid):
        cat = CatagoryModel.findById(catid)
        if not bool(cat):
            return gettex('NOT_FOUND'),404

        return CatagorySchema().dump(cat)

    @IsAdminMiddleware.PermissionMiddleware
    def put(self,catid):
        data = parser.parse_args()
        cat = CatagoryModel.findById(catid)
        if not bool(cat):
            return gettex('NOT_FOUND'),404
        
        cat.catName = data.catName
        try:
            cat.insert()
        except:
            return gettex('SOMETHING_WRONG'),500

        return CatagorySchema().dump(cat)

    @IsAdminMiddleware.PermissionMiddleware
    def delete(self,catid):
        cat = CatagoryModel.findById(catid)
        if not bool(cat):
            return gettex('NOT_FOUND'),404
        
        try:
            cat.delete()
        except:
            return gettex('SOMETHING_WRONG'),500
        
        return CatagorySchema().dump(cat)

        




    
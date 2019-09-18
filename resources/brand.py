from schema.brand import BrandModel, BrandSchema
from resources.module import (
    req, gettex, db, IsAdminMiddleware, reqparse,Resource,uuid4
)

parser = reqparse.RequestParser()
parser.add_argument('brandName', required=True)


class BrandResource(Resource):

    @classmethod
    @IsAdminMiddleware.PermissionMiddleware
    def get(cls):
        brand = BrandModel.fetchAll()
        return BrandSchema(many=True).dump(brand)

    @classmethod
    @IsAdminMiddleware.PermissionMiddleware
    def post(cls):
        dataBody = parser.parse_args()
        brand = BrandSchema().load(dataBody, session=db.session)

        isExist = bool(BrandModel.findByBrandName(dataBody.brandName))
        if isExist:
            return gettex('EXIST'), 422
        try:
            brand.insert()
        except:
            return gettex('SOMETHING_WRONG'),500

        return BrandSchema().dump(brand)

class AbsBrandResource(Resource):

    @IsAdminMiddleware.PermissionMiddleware
    def get(self,brandid):
        
        data = BrandModel.findById(brandid)
        if data is None:
            return gettex('NOT_FOUND'),404
        
        return BrandSchema().dump(data)

    @IsAdminMiddleware.PermissionMiddleware
    def put(self,brandid):

        value = parser.parse_args()
        data = BrandModel.findById(brandid)
        dataName = BrandModel.findByBrandName(value.brandName)

        if data is None:
            return gettex('NOT_FOUND'),404
            
        data.brandName = value.brandName
        try:
            data.insert()
        except:
            return gettex('SOMETHING_WRONG'),500

        return BrandSchema().dump(data)
    
    @IsAdminMiddleware.PermissionMiddleware
    def delete(self,brandid):
        data = BrandModel.findById(brandid)
        if data is None:
            return gettex('NOT_FOUND'),404
        
        data.delete()
        return BrandSchema().dump(data)
    

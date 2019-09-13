from schema.brand import BrandModel,BrandSchema
from resources.module import Resource
from resources.module import (
    req,gettex,db,jwt_required,get_jwt_claims,IsAdminMiddleware as Middleware
)

class BrandResource(Resource):
    
    @classmethod
    @Middleware.PermissionMiddleware
    def get(cls):
        brand = BrandModel.fetchAll()
        return BrandSchema(many=True).dump(brand)

    @classmethod
    @jwt_required
    def post(cls):
        user = get_jwt_claims()
        if user['role']:
            dataBody = req.get_json()
            brand = BrandSchema().load(dataBody,session=db.session)

            isExist = BrandModel.findByBrandName(dataBody['brandName'])
            if isExist is not None:
                return gettex('EXIST'),404
            
            brand.insert()
            return BrandSchema().dump(brand)
        
        return gettex('DENIAL'),401


from schema.products import ProductModel,ProductSchema
from model.user import UserModel
from model.catagories import CatagoryModel
from model.store import StoreModel
from resources.module import (
    req,Resource,db,gettex,jwt_required,UserMiddleware
)

class ProductResource(Resource):

    model = ProductModel
    schema = ProductSchema
    user = UserModel
    cat = CatagoryModel
    store = StoreModel
    
    @classmethod
    @UserMiddleware.userDetail
    def get(cls):
        data = cls.model.fetchAll()
        return cls.schema(many=True).dump(data)

    @classmethod
    @UserMiddleware.userDetail
    def post(cls):

        value = req.get_json()
        product = cls.schema().load(value,partial=('proId',))
        isUserId = bool(value.get('userId'))
        isStoreId = bool(value.get('storeId'))

        if not bool(value.get('catId')):
            return gettex('NOT_FOUND'),404

        isCatId = cls.cat.findById(value['catId'])
        if not bool(isCatId):
            return gettex('NOT_FOUND'),404

        if isUserId:
            userid = value['userId']
            isExistUserId = bool(cls.user.findById(userid))
            proId = cls.model.newProid(userid)
            islimit = cls.model.isLimit(userid) 

            if not isExistUserId:
                return gettex('NOT_FOUND'),422

            if islimit:
                return gettex('LIMITED'),401

        if isStoreId:
            storeid = value['storeId']
            isExistStoreId = cls.store.findByStoreId(storeid)
            if not bool(isExistStoreId):
                return gettex('NOT_FOUND'),404

            proId = cls.model.newProid(storeid)

        value.update({'proId':proId})
        product = cls.schema().load(value,session=db.session)

        try:
            product.insert()
        except:
            return gettex('SOMETHING_WRONG'),500

        return cls.schema().dump(product)

class AbsProductResource(ProductResource):

    @classmethod
    @UserMiddleware.userDetail
    def get(cls,productid):
        product = cls.model.findByProId(productid)
        if not bool(product):
            return gettex('NOT_FOUND'),404
        
        return cls.schema().dump(product)
    
    @classmethod
    @UserMiddleware.userDetail
    def delete(cls,productid):
        product = cls.model.findByProId(productid)
        if not bool(product):
            return gettex('NOT_FOUND'),404
        
        try:
            product.delete()
        except:
            return gettex('SOMETHING_WRONG'),500
        
        return gettex('SUCCESS'),201
        
    @classmethod
    @UserMiddleware.userDetail
    def put(cls,productid):
        value = req.get_json()
        product = cls.model.findByProId(productid)
        if not bool(product):
            return gettex('NOT_FOUND'),404

        try:    
            product.proName = value['proName']
            product.proPrice = value['proPrice']
            product.proImg = value['proImg']
            product.proQuantity = value['proQuantity']
            product.feature = value['feature']
            product.desc = value['desc']
            product.insert()
        except:
            return gettex('SOMETHING_WRONG'),500
        
        return cls.schema().dump(product)
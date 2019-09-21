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
    
    @UserMiddleware.userDetail
    def get(self):
        data = self.model.fetchAll()
        return self.schema(many=True).dump(data)

    @UserMiddleware.userDetail
    def post(self):

        vl = req.get_json()
        isUserId = bool(vl[0].get('userId'))
        isStoreId = bool(vl[0].get('storeId'))

        if isStoreId:
            authorId = vl[0]['storeId']
            isExistStoreId = self.store.findByStoreId(authorId)
            if not bool(isExistStoreId):
                return gettex('NOT_FOUND'),404
        else:
            authorId = vl[0]['userId']
            isExistUserId = bool(self.user.findById(authorId))
            islimit = self.model.isLimit(authorId) 
            
            if not isExistUserId:
                return gettex('NOT_FOUND'),422

            if islimit:
                return gettex('LIMITED'),401

        serial = self.model.findSerial()
        for value in vl:
            serial += 1
            proId = self.model.newProid(authorId,serial)
            value.update({'proId':proId})
        
        product = self.schema(many=True).load(vl,session=db.session)
        try:
            self.model.insertMany(product)
        except:
            return gettex('SOMETHING_WRONG'),500

        return gettex('SUCCESS'),201

class AbsProductResource(ProductResource):

    @UserMiddleware.userDetail
    def get(self,productid):
        product = self.model.findByProId(productid)
        if not bool(product):
            return gettex('NOT_FOUND'),404
        
        return self.schema().dump(product)
    
    @UserMiddleware.userDetail
    def delete(self,productid):
        product = self.model.findByProId(productid)
        if not bool(product):
            return gettex('NOT_FOUND'),404
        
        try:
            product.delete()
        except:
            return gettex('SOMETHING_WRONG'),500
        
        return gettex('SUCCESS'),201
        
    @UserMiddleware.userDetail
    def put(self,productid):
        value = req.get_json()
        product = self.model.findByProId(productid)
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
        
        return self.schema().dump(product)
from schema.store import StoreModel,StoreSchema
from schema.user import UserModel
from resources.module import (
    reqparse,Resource,gettex,db,req,jwt_required,time
)



class StoreResource(Resource):
    
    @classmethod
    def get(cls):
        data = StoreModel.fetchAll()
        return StoreSchema(many=True).dump(data)

    @classmethod
    @jwt_required
    def post(cls):
        data = req.get_json()
        store = StoreSchema().load(data,partial=('storeId',))
        try:
            isExist = StoreModel.findByStoreName(data['storeName'])
            user = UserModel.findById(data['userId'])
            islimit = StoreModel.findByUserId(data['userId'])
        except:
            return gettex('SOMETHING_WRONG'),500
        
        if bool(isExist):
            return gettex('EXIST'),422

        if not bool(user):
            return gettex('NOT_EXIST'),404
        
        if islimit:
            return gettex('LIMITED'),422

        try:
            storeId = f"ST_{store.findSerial() + 1}_{int(time())}_{user.userId}"
            store.storeId = storeId
            store.insert()
        except:
            return gettex('SOMETHING_WRONG'),500

        return StoreSchema().dump(store) 


class AbsStoreResource(Resource):

    @jwt_required
    def get(cls,storeid):
        data = StoreModel.findByStoreId(storeid)
        if not bool(store):
            return gettex('NOT_FOUND'),404
        
        return StoreSchema().dump(data)
    
    @jwt_required
    def put(cls,storeid):
        data = req.get_json()
        store = StoreModel.findByStoreId(storeid)
        if not bool(store):
            return gettex('NOT_FOUND'),404

        try:
            store.storePicture = data['storePicture'] or None
            store.storeCoverImage = data['storeCoverImage'] or None
            store.storeLocation = data['storeLocation'] or None
            store.storeName = data['storeName']
            store.insert()
        except:
            return gettex('SOMETHING_WRONG'),500

        return StoreSchema().dump(store)
    
    @jwt_required
    def delete(cls,storeid):
        store = StoreModel.findByStoreId(storeid)
        if not bool(store):
            return gettex('NOT_FOUND'),404
        
        try:
            store.delete()
        except:
            return gettex('SOMETHING_WRONG'),500

        return StoreSchema().dump(store)
        

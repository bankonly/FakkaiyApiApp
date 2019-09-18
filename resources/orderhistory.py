from schema.orderhistory import OrderHistoryModel,OrderHistorySchema
from resources.module import (
    req,reqparse,Resource,gettex,db
)
from model.order import OrderModel
from model.products import ProductModel

class OrderHistoryResource(Resource):
    
    model = OrderHistoryModel
    schema = OrderHistorySchema
    order = OrderModel
    product = ProductModel

    @classmethod
    def get(cls):
        data = cls.model.fetchAll()
        return cls.schema(many=True).dump(data)

    @classmethod
    def post(cls):
        value = req.get_json()
        if not bool(value.get('orderId')) or not bool(value.get('proId')):
            return gettex('NOT_FOUND'),404

        isExistOrderId = cls.order.findById(value['orderId'])
        isExistProId = cls.product.findByProId(value['proId'])

        if not bool(isExistOrderId) or not bool(isExistProId):
            return gettex('NOT_FOUND'),404

        data = cls.schema().load(value,session=db.session)
        try:
            data.insert()
        except:
            return gettex('SOMETHING_WRONG'),500
        
        return cls.schema().dump(data)

class AbsOrderHistoryResource(OrderHistoryResource):
    
    @classmethod
    def get(cls,orderid):
        data = cls.model.fetchById(orderid)
        if not bool(data):
            return gettex('NOT_FOUND'),404

        return cls.schema().dump(data)

    @classmethod
    def delete(cls,orderid):
        data = cls.model.fetchById(orderid)
        if not bool(data):
            return gettex('NOT_FOUND'),404
        try:
            data.delete()
        except:
            return gettex('SOMETHING_WRONG'),500

        return gettex('SUCCESS'),201

    @classmethod
    def put(cls,orderid):
        pass





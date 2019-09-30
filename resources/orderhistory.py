from schema.orderhistory import OrderHistoryModel,OrderHistorySchema
from resources.module import (
    req,reqparse,Resource,gettex,db
)
from model.order import OrderModel
from model.products import ProductModel

class OrderHistoryResource(Resource):

    def get(self):
        data = OrderHistoryModel.fetchAll()
        return OrderHistorySchema(many=True).dump(data)

    def post(self):
        vl = req.get_json()

        for value in vl:
            if not bool(value.get('orderId')) or not bool(value.get('proId')):
                return gettex('NOT_FOUND'),404

            isExistOrderId = OrderModel.findById(value['orderId'])
            isExistProId = ProductModel.findByProId(value['proId'])
            if not bool(isExistOrderId) or not bool(isExistProId):
                return gettex('NOT_FOUND'),404

        data = OrderHistorySchema(many=True).load(vl,session=db.session)
        try:
            OrderHistoryModel.insertMany(data)
        except:
            return gettex('SOMETHING_WRONG'),500

        return gettex('SUCCESS'),201

class AbsOrderHistoryResource(OrderHistoryResource):
    
    def get(self,orderid):
        data = OrderHistoryModel.fetchById(orderid)
        if not bool(data):
            return gettex('NOT_FOUND'),404

        return OrderHistorySchema.dump(data)

    def delete(self,orderid):
        data = OrderHistoryModel.fetchById(orderid)
        if not bool(data):
            return gettex('NOT_FOUND'),404
        try:
            data.delete()
        except:
            return gettex('SOMETHING_WRONG'),500

        return gettex('SUCCESS'),201

    def put(self,orderid):
        pass





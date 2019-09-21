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

    def get(self):
        data = self.model.fetchAll()
        return self.schema(many=True).dump(data)

    def post(self):
        vl = req.get_json()

        for value in vl:
            if not bool(value.get('orderId')) or not bool(value.get('proId')):
                return gettex('NOT_FOUND'),404

            isExistOrderId = self.order.findById(value['orderId'])
            isExistProId = self.product.findByProId(value['proId'])
            if not bool(isExistOrderId) or not bool(isExistProId):
                return gettex('NOT_FOUND'),404

        data = self.schema(many=True).load(vl,session=db.session)
        try:
            self.model.insertMany(data)
        except:
            return gettex('SOMETHING_WRONG'),500

        return gettex('SUCCESS'),201

class AbsOrderHistoryResource(OrderHistoryResource):
    
    def get(self,orderid):
        data = self.model.fetchById(orderid)
        if not bool(data):
            return gettex('NOT_FOUND'),404

        return self.schema().dump(data)

    def delete(self,orderid):
        data = self.model.fetchById(orderid)
        if not bool(data):
            return gettex('NOT_FOUND'),404
        try:
            data.delete()
        except:
            return gettex('SOMETHING_WRONG'),500

        return gettex('SUCCESS'),201

    def put(self,orderid):
        pass





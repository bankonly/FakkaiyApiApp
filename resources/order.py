from schema.order import OrderModel,OrderSchema
from resources.module import (
    req,reqparse,gettex,db,Resource
)
from model.user import UserModel

parser = reqparse.RequestParser()
parser.add_argument('userId',required=True)



class OrderResource(Resource):
    
    model = OrderModel
    schema = OrderSchema
    user = UserModel

    @classmethod
    def get(cls):
        data = cls.model.fetchAll()
        return cls.schema(many=True).dump(data) 

    @classmethod
    def post(cls):
        value = parser.parse_args()

        isUserId = cls.user.findById(value.userId)
        if not bool(isUserId):
            return gettex('NOT_FOUND'),404
        

        orderid = cls.model.generateId(value.userId)
        value.update({'orderId':orderid})
        order = cls.schema().load(value,session=db.session)

        try:
            order.insert()
        except:
            return gettex('SOMETHING_WRONG'),500
        
        return cls.schema().dump(order)


class AbsOrderResource(OrderResource):
    
    @classmethod
    def get(cls,orderid):
        order = cls.model.findById(orderid)
        if not bool(order):
            return gettex('NOT_FOUND'),404
        
        return cls.schema().dump(order)

    @classmethod
    def delete(cls,orderid):
        order = cls.model.findById(orderid)
        if not bool(order):
            return gettex('NOT_FOUND'),404
        
        try:
            order.delete()
        except:
            return gettex('SOMETHING_WRONG'),500

        return gettex('SUCCESS'),201

    @classmethod
    def put(cls,orderid):
        pass 
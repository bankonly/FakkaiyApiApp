from config.ma import ma
from model.order import OrderModel

class OrderSchema(ma.ModelSchema):
    class Meta:
        model = OrderModel
        include_fk = True
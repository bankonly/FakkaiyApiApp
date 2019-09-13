from config.ma import ma
from model.orderhistory import OrderHistoryModel

class OrderHistorySchema(ma.ModelSchema):
    class Meta:
        model = OrderHistoryModel
        include_fk = True
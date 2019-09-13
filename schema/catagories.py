from config.ma import ma
from model.catagories import CatagoryModel

class CatagorySchema(ma.ModelSchema):
    class Meta:
        model = CatagoryModel
        include_fk = True
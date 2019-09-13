from config.ma import ma
from model.store import StoreModel

class StoreSchema(ma.ModelSchema):
    class Meta:
        model = StoreModel
        include_fk = True
from config.ma import ma
from model.store import StoreModel

class StoreSchema(ma.ModelSchema):
    class Meta:
        model = StoreModel
        load_only = ('user',)
        include_fk = True
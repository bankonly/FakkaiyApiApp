from config.ma import ma
from model.brand import BrandModel

class BrandSchema(ma.ModelSchema):
    class Meta:
        model = BrandModel
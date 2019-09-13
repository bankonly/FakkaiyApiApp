from config.ma import ma
from model.products import ProductModel

class ProductSchema(ma.ModelSchema):
    class Meta:
        model = ProductModel
        include_fk = True
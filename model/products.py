from config.db import db
from model.store import StoreModel
from time import time

class ProductModel(db.Model):
    __tablename__ = "products"

    proId = db.Column(db.String(80),nullable=False,primary_key=True) # PROD_ + serial + authorId + 
    proName = db.Column(db.String(50),nullable=False)
    proPrice = db.Column(db.DECIMAL(18,2),nullable=False,default="0")
    proImg = db.Column(db.Text,nullable=True,default=None)
    proQuantity = db.Column(db.Integer,default='1')
    feature = db.Column(db.Text,nullable=True,default=None)
    flashSaleStatus = db.Column(db.Boolean,default=False)
    authorId = db.Column(db.String(80),nullable=False)
    desc = db.Column(db.Text,nullable=True,default=None)

    createDate = db.Column(db.BigInteger,default=int(time()))
    updateDate = db.Column(db.BigInteger,onupdate=int(time()))
    
    catId = db.Column(db.Integer,db.ForeignKey('catagories.catId'),nullable=False,)
    userId = db.Column(db.String(80),db.ForeignKey('users.userId'),nullable=False,)
    storeId = db.Column(db.String(80),db.ForeignKey('store.storeId'),nullable=False,)
    brandId = db.Column(db.String(80),db.ForeignKey('brands.brandId'),nullable=True,default='0',)
    

    catagory = db.relationship('CatagoryModel')
    user = db.relationship('UserModel')
    brand = db.relationship('BrandModel')
    store = db.relationship(StoreModel)
    

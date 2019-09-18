from config.db import db
from model.store import StoreModel
from time import time
from model.catagories import CatagoryModel
from model.brand import BrandModel
from model.order import OrderHistoryModel

class ProductModel(db.Model):
    __tablename__ = "products"

    proId = db.Column(db.String(80),nullable=False,primary_key=True) # PROD_ + serial + pro_name + userId or storeId
    proName = db.Column(db.String(50),nullable=False)
    proPrice = db.Column(db.Float,nullable=False,default="0")
    proImg = db.Column(db.Text,nullable=True,default=None)
    proQuantity = db.Column(db.Integer,default='1')
    feature = db.Column(db.Text,nullable=True,default=None)
    flashSaleStatus = db.Column(db.Boolean,default=False)
    # authorId = db.Column(db.String(80),nullable=False)
    desc = db.Column(db.Text,nullable=True,default=None)

    createDate = db.Column(db.BigInteger,default=time)
    updateDate = db.Column(db.BigInteger,onupdate=time)
    
    catId = db.Column(db.String(80),db.ForeignKey('catagories.catId'),nullable=False,)
    userId = db.Column(db.String(80),db.ForeignKey('users.userId'),nullable=True,)
    storeId = db.Column(db.String(80),db.ForeignKey('store.storeId'),nullable=True,)
    brandId = db.Column(db.String(80),db.ForeignKey('brands.brandId'),nullable=True,default='0',)
    

    catagory = db.relationship(CatagoryModel)
    user = db.relationship('UserModel')
    brand = db.relationship('BrandModel')
    store = db.relationship(StoreModel)
    orderhistory = db.relationship(OrderHistoryModel,lazy="dynamic",cascade="all ,delete-orphan")
    
    @classmethod
    def newProid(cls,authorid): 
        return f"PROD_{cls.findSerial()}_{int(time())}_{authorid}"
    @classmethod
    def findSerial(cls):
        return cls.query.count()

    @classmethod
    def fetchAll(cls):
        return cls.query.order_by(cls.createDate.desc()).all()

    @classmethod
    def findByProId(cls,proid):
        return cls.query.filter_by(proId=proid).first()

    @classmethod
    def isLimit(cls,userid) -> bool:
        return cls.query.filter_by(userId=userid).count() > 10

    @classmethod
    def findByUserId(cls,userid):
        return cls.query.filter_by(userId=userid).order_by(cls.createDate.desc())

    @classmethod
    def findByStoreId(cls,storeid):
        return cls.query.filter_by(storeId=storeid).all()    

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
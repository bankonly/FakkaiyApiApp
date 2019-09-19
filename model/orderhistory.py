from config.db import db
from time import time

class OrderHistoryModel(db.Model):
    __tablename__ = 'orderhistories'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    quantity = db.Column(db.Integer,nullable=False)
    flaskSaleStatus = db.Column(db.Boolean,nullable=False)

    createDate = db.Column(db.BigInteger,default=time)
    updateDate = db.Column(db.BigInteger,onupdate=time)

    orderId = db.Column(db.String(80),db.ForeignKey('orders.orderId')) 
    proId = db.Column(db.String(80),db.ForeignKey('products.proId')) 
    
    order = db.relationship('OrderModel')
    product = db.relationship('ProductModel')

    @classmethod
    def fetchAll(cls):
        return cls.query.all()

    @classmethod
    def fetchById(cls,_id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def fetchByOrderId(cls,orderid):
        return cls.query.filter_by(orderId=orderid).all()

    @classmethod
    def fetchByProId(cls,proid):
        return cls.query.filter_by(proId=proid).all()
    
    def insertMany(self,value):
        db.session.insert().values(value)
        db.session.commit()

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    






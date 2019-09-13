from config.db import db
from time import time

class OrderHistoryModel(db.Model):
    __tablename__ = 'orderhistories'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    quantity = db.Column(db.Integer,nullable=False)
    flaskSaleStatus = db.Column(db.Boolean,default=False)

    createDate = db.Column(db.BigInteger,default=int(time()))
    updateDate = db.Column(db.BigInteger,onupdate=int(time()))

    orderId = db.Column(db.String(80),db.ForeignKey('orders.orderId')) #userid + time()
    order = db.relationship('OrderModel')

    @classmethod
    def fetchAll(cls):
        return cls.query.all()

    @classmethod
    def fetchById(self,_id):
        return cls.query.filter_by(id=_id).all()

    @classmethod
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    






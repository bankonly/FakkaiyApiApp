from config.db import db
from time import time

class OrderModel(db.Model):
    __tablename__ = 'orders'

    orderId = db.Column(db.String(80),primary_key=True) #userid + time() + 

    createDate = db.Column(db.BigInteger,default=time)
    updateDate = db.Column(db.BigInteger,onupdate=time)

    userId = db.Column(db.String(50),db.ForeignKey('users.userId'))
    user = db.relationship('UserModel')

    @classmethod
    def fetchAll(cls):
        return cls.query.all()

    @classmethod
    def findById(cls,orderid):
        return cls.query.filter_by(orderId=orderid).first()

    @classmethod
    def findByUserId(cls,userid):
        return cls.query.filter_by(userId=userid).all()

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    






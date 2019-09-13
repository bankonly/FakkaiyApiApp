from config.db import db
from time import time
from uuid import uuid4

class BrandModel(db.Model):
    __tablename__ = 'brands'

    brandId = db.Column(db.String(80),primary_key=True,nullable=False,default=uuid4().hex)
    brandName = db.Column(db.String(50),nullable=False)

    createDate = db.Column(db.BigInteger,default=int(time()))
    updateDate = db.Column(db.BigInteger,onupdate=int(time()))

    @classmethod
    def fetchAll(cls):
        return cls.query.all()

    @classmethod
    def findById(cls,brandid):
        return cls.query.filter_by(brandId=brandid).first()

    @classmethod
    def findByBrandName(cls,name):
        return cls.query.filter_by(brandName=name).first()
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    






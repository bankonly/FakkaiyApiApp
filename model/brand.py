from config.db import db
from time import time
from config.app import uuid4
from helper.defaultfunc import DefaultFunc
class BrandModel(db.Model):
    __tablename__ = 'brands'

    brandId = db.Column(db.String(80),primary_key=True,nullable=False,default=DefaultFunc.generateId)
    brandName = db.Column(db.String(50),nullable=False)

    createDate = db.Column(db.BigInteger,default=time)
    updateDate = db.Column(db.BigInteger,onupdate=time)

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
    






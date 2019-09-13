from config.db import db
from time import time

class CatagoryModel(db.Model):
    __tablename__ = 'catagories'

    catId = db.Column(db.Integer,primary_key=True,autoincrement=True)
    catName = db.Column(db.String(50),nullable=False)
    
    createDate = db.Column(db.BigInteger,default=int(time()))
    updateDate = db.Column(db.BigInteger,onupdate=int(time()))

    @classmethod
    def fetchAll(cls):
        return cls.query.all()

    @classmethod
    def findById(cls,catid):
        return cls.query.filter_by(catId=catid).first()

    @classmethod
    def findByName(cls,name):
        return cls.query.filter_by(catName=name).first()

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    






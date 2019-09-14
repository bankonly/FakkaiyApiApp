from config.db import db
from time import time

class StoreModel(db.Model):
    __tablename__ = "store"

    storeId = db.Column(db.String(80),primary_key=True) # prefix ST_ + Serial +  registerDate(from UserModel) + userId
    storeName = db.Column(db.String(40),nullable=False)
    storeLocation = db.Column(db.Text,nullable=True)
    storeCoverImage = db.Column(db.Text,nullable=True)
    storePicture = db.Column(db.Text,nullable=True)

    createDate = db.Column(db.BigInteger,default=time)
    updateDate = db.Column(db.BigInteger,onupdate=time)

    userId = db.Column(db.String(50),db.ForeignKey('users.userId'))
    user = db.relationship('UserModel')

    @classmethod
    def fetchAll(cls):
        return cls.query.all()
    
    @classmethod
    def findSerial(cls):
        return cls.query.count()

    @classmethod
    def findByStoreId(cls,storeid):
        return cls.query.filter_by(storeId=storeid).first()

    @classmethod
    def findByUserId(cls,userid) -> bool:
        return cls.query.filter_by(userId=userid).count() >= 5
    
    @classmethod
    def findByStoreName(cls,storename):
        return cls.query.filter_by(storeName=storename).first()

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
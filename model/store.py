from config.db import db
from time import time

class StoreModel(db.Model):
    __tablename__ = "store"

    storeId = db.Column(db.String(80),primary_key=True) # prefix ST_ + Serial +  registerDate(from UserModel) + userId
    storeName = db.Column(db.String(40),nullable=False)
    storeLocation = db.Column(db.Text,nullable=True)
    storeCoverImage = db.Column(db.Text,nullable=True)
    storePicture = db.Column(db.Text,nullable=True)

    createDate = db.Column(db.BigInteger,default=int(time()))
    updateDate = db.Column(db.BigInteger,onupdate=int(time()))

    userId = db.Column(db.String(50),db.ForeignKey('users.userId'))
    user = db.relationship('UserModel')
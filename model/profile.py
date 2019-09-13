from config.db import db
from time import time

class ProfileModel(db.Model):
    __tablename__ = 'profile'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    lastname = db.Column(db.String(80),nullable=True)
    facebook = db.Column(db.String(80),nullable=True)
    instragram = db.Column(db.String(80),nullable=True)
    location = db.Column(db.Text,nullable=True)
    avatar = db.Column(db.Text,nullable=True)
    
    createDate = db.Column(db.BigInteger,default=int(time()))
    updateDate = db.Column(db.BigInteger,onupdate=int(time()))

    userId = db.Column(db.String(50),db.ForeignKey('users.userId'))
    user = db.relationship('UserModel')

    @classmethod
    def findById(cls,userid):
        return cls.query.filter_by(userId=userid).first()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


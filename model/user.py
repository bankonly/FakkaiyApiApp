from config.db import db
from model.profile import ProfileModel
from config.app import uuid4
from time import time
from helper.defaultfunc import DefaultFunc


class UserModel(db.Model):
    __tablename__ = 'users'

    userId = db.Column(db.String(50),primary_key=True,default=DefaultFunc.generateId)
    password = db.Column(db.String(80),nullable=True)
    email = db.Column(db.String(80),nullable=False)
    name = db.Column(db.String(50),nullable=True)
    role = db.Column(db.SmallInteger,default='0')

    createDate = db.Column(db.BigInteger,default=time)
    updateDate = db.Column(db.BigInteger,onupdate=time)

    profile = db.relationship(ProfileModel,lazy="dynamic",cascade="all ,delete-orphan")

    @classmethod
    def fetchAll(cls):
        return cls.query.all()

    @classmethod    
    def findById(cls,userid) -> "UserModel":
        return cls.query.filter_by(userId=userid).first()

    @classmethod    
    def findByEmail(cls,email) -> "UserModel":
        return cls.query.filter_by(email=email).first()

    @classmethod    
    def findByName(cls,name) -> "UserModel":
        return cls.query.filter_by(name=name).first()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    




    

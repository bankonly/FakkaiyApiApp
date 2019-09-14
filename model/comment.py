from config.db import db
from time import time
from model.products import ProductModel

class CommentModel(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    commentId = db.Column(db.String(70),primary_key=True) #userid + time()
    commentRating = db.Column(db.Integer,default='0')
    commentMsg = db.Column(db.Text,nullable=False)
    userId = db.Column(db.String(50),db.ForeignKey('users.userId'))
    proId = db.Column(db.String(50),db.ForeignKey('products.proId'))

    createDate = db.Column(db.BigInteger,default=time)
    updateDate = db.Column(db.BigInteger,onupdate=time)
    
    user = db.relationship('UserModel')
    product = db.relationship(ProductModel)

    @classmethod
    def fetchAll(cls):
        return cls.query.all()

    @classmethod
    def fetchByUser(self,userid):
        return cls.query.filter_by(userId=userid).all()

    @classmethod
    def fetchByProduct(self,proid):
        return cls.query.filter_by(userId=proid).all()
    
    @classmethod
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    






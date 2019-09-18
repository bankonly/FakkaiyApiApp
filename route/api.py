from config.app import api
from route.module import *

# api authenticate
api.add_resource(Authenticate,'/login')

# api route
api.add_resource(HomeResource,'/')

# user resource
api.add_resource(UserResource,'/api/users')
api.add_resource(InheritUserResource,'/api/users/<userid>')

# profile resource
api.add_resource(ProfileResource,'/api/profile')


# BrandResource 
api.add_resource(BrandResource,'/api/brand')
api.add_resource(AbsBrandResource,'/api/brand/<brandid>')

# CatagoryResource 
api.add_resource(CatagoryResource,'/api/catagories')
api.add_resource(AbsCatagoryResource,'/api/catagories/<catid>')

# CommentResource 
api.add_resource(CommentResource,'/api/comment')

# OrderResource 
api.add_resource(OrderResource,'/api/order')
api.add_resource(AbsOrderResource,'/api/order/<orderid>')

# OrderHistoryResource 
api.add_resource(OrderHistoryResource,'/api/orderhistory')
api.add_resource(AbsOrderHistoryResource,'/api/orderhistory/<orderid>')

# ProductResource 
api.add_resource(ProductResource,'/api/product')
api.add_resource(AbsProductResource,'/api/product/<productid>')

# StoreResource 
api.add_resource(StoreResource,'/api/store')
api.add_resource(AbsStoreResource,'/api/store/<storeid>')



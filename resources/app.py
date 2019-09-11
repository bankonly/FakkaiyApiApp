from flask_restful import Resource
from config.strings import gettex

class HomeResource(Resource):
    
    @classmethod
    def get(cls):
        return f"Hello world"
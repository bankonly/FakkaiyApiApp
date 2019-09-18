from config.app import jwt_required,get_jwt_claims
from config.strings import gettex
from flask import request


class UserMiddleware:

    def userDetail(callback):
        @jwt_required
        def detail(*arg,**kwarg):
            request.user = get_jwt_claims()
            return callback(*arg,**kwarg)

        return detail

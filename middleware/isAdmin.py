from config.app import jwt_required,get_jwt_claims
from config.strings import gettex


class IsAdminMiddleware:

    def PermissionMiddleware(callback):
        @jwt_required
        def isAdmin(*arg,**kwarg):
            user = get_jwt_claims()
            if not user['role']:
                return gettex('DENIAL'),401
            return callback(*arg,**kwarg)
            
        return isAdmin

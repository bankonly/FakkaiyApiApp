from config.ma import ma
from model.user import UserModel

class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        # dump_only = ('userProfile',)
        load_only = ('password',)


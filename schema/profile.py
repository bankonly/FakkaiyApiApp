from config.ma import ma
from model.profile import ProfileModel

class ProfileSchema(ma.ModelSchema):
    class Meta:
        model = ProfileModel
        load_only = ('user',)
        include_fk = True

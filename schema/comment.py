from config.ma import ma
from model.comment import CommentModel

class CommentSchema(ma.ModelSchema):
    class Meta:
        model = CommentModel
        include_fk = True
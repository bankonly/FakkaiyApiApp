from flask_marshmallow import Marshmallow
from config.app import app
from marshmallow import ValidationError

ma = Marshmallow(app)


@app.errorhandler(ValidationError)
def errorhandler(err):
    return err.messages

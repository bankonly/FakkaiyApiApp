from config.app import app,jwt,socketio,migrate
from config.ma import ma
from config.db import db
from route.api import api


@app.before_first_request
def before_first_request():
    pass

@app.errorhandler
def errorhandler():
    return "There is an error"

if __name__ == "__main__":
    
    ma.init_app(app)
    db.init_app(app)

    socketio.run(app,port=5000,debug=True)
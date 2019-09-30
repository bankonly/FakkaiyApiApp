import os
import json

from config.app import app
from flask import request
from config.strings import gettex
from helper.fileupload import FileUpload,FileUploadBase64
from config.app import socketio
from config.apschedule import schedule
from config.db import OperationalError

@app.route('/uploadImage',methods = ['POST'])
def upload():
    # isDecoded = FileUploadBase64(request.get_json()['img']).convertFromBase64()
    # return 'success' 
    isupload = FileUpload(request.files).uploadImage()
    print(isupload)
    return 'success'

@app.route('/runschedule')
def sendmsg(msg="Hello worldd er"):
    print(msg)
    return msg

@socketio.on('runschedule')
def testing(msg):
    msg = sendmsg()
    socketio.emit('emitrunschedule',{
        "data":msg
    },broadcast=True)

# schedule.add_job(func=sendmsg,trigger='cron',second="*/5",id="runschedule")
# schedule.remove_job("runschedule")

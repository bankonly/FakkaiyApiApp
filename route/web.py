import os
import json

from config.app import app
from flask import request
from config.strings import gettex
from helper.fileupload import FileUpload
from config.app import socketio
from config.apschedule import schedule

@app.route('/uploadImage',methods = ['POST'])
def upload():
    isUploaded = FileUpload(files=request.files).uploadImage()
    if isUploaded == 0:
        return gettex('SOMETHING_WRONG'),500

    return isUploaded

@app.route('/runschedule')
def sendmsg(msg="Hello worldd er"):
    print(msg)
    return msg

@socketio.on('runschedule')
def runfuncs(msg):
    msg = sendmsg()
    socketio.emit('emitrunschedule',{
        "data":msg
    },broadcast=True)

# schedule.add_job(func=sendmsg,trigger='cron',second="*/5",id="runschedule")
# schedule.remove_job("runschedule")
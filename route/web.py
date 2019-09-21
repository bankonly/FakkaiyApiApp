import os
import json

from config.app import app
from flask import request
from config.strings import gettex
from helper.fileupload import FileUpload


@app.route('/uploadImage',methods = ['POST'])
def upload():
    
    isUploaded = FileUpload(request.files).uploadImage()
    if isUploaded == 0:
        return gettex('SOMETHING_WRONG'),500

    return isUploaded

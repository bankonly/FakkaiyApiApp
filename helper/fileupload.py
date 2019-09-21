import os

from uuid import uuid4
from config.app import app, ALLOWED_TYPE
from config.strings import gettex
from werkzeug.utils import secure_filename

class FileUpload:

    def __init__(self,files):
        self.reqfile = files

    def allowedFile(self,filename):
        fileType = filename.split('.')[-1]
        if fileType.lower() not in ALLOWED_TYPE:
            return False
        
        return True

    def uploadImage(self):
        if 'file' not in self.reqfile:
            return gettex('NOT_FOUND'),404

        files = self.reqfile['file']
        isExist = bool(files.filename)
    
        if not isExist:
            return gettex('NOT_FOUND'),404
    
        isAllowed = self.allowedFile(files.filename)
        if isAllowed:
            filename = secure_filename(files.filename)
            try:
                files.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            except:
                return 0
        return filename
        
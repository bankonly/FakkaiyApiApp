import os
import time
import base64

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

class FileUploadBase64:

    def __init__(self,base64img):
        self.base64img = base64img

    def isAllowed(self,fileType):
        if fileType.lower() not in ALLOWED_TYPE:
            return False
        return True

    def convertFromBase64(self):
        fileType = self.base64img.split('/')[1].split(';')[0]
        base64encode = base64.b64decode(self.base64img.decode('utf-8'))
        
        if self.isAllowed(fileType):
            with open(f'storage/imgs/{int(time.time())}.{fileType}','wb') as writeFile:
                writeFile.write(base64encode)

        
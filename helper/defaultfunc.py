from uuid import uuid4
from config.app import ALLOWED_TYPE
from config.strings import gettex
class DefaultFunc:

    def generateId():
        return uuid4().hex
        
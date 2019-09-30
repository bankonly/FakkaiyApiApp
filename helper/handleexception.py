from config.strings import gettex
class HandleExcetion:
    
    def output(msg):
        print('----------------ERROR----------------')
        print(msg)
        print('----------------ERROR----------------')
        return gettex('SOMETHING_WRONG')


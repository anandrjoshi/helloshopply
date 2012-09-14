from pyes import *

class Model(object):

    def __init__(self):
        self.conn = ES(['localhost:9200'])
        
    def get_message(self):  
        return self.conn.collect_info()

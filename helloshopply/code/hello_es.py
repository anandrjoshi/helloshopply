from pyes import *

class Model(object):

    def __init__(self):
        self.conn = ES(['172.25.243.91:9200'])
        
    def get_message(self):  
        return self.conn.collect_info()

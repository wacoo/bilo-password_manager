import pymongo

class DB(object):
    URL = 'mongo://127.0.0.2:27017'
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(DB.URL)
        DB.DATABASE = client['bilo_db']

    @staticmethod
    def insert(collection, data):
        DB.DATABASE[collection].insert(data)
    
    @staticmethod
    def search(collection, query):
        return DB.DATABASE[collection].find(query)
    
    @staticmethod
    def search_one(collection, query):
        return DB.DATABASE[collection].find_one(query)

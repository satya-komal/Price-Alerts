import pymongo

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    dbName = None

    @staticmethod
    def initialise():
        client = pymongo.MongoClient(Database.URI)
        Database.dbName =client['full_stack']

    @staticmethod
    def insert(collection,data):
        Database.dbName[collection].insert(data)

    @staticmethod
    def find(collection,query):
        return Database.dbName[collection].find(query)

    @staticmethod
    def find_one(collection,query):
        return Database.dbName[collection].find_one(query)

    @staticmethod
    def update(collection,query,data):
        Database.dbName[collection].update(query,data,upsert=True)
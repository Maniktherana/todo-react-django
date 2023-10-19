from pymongo import MongoClient


class MongoConnection:
    def __init__(self, host, port, db_name, collection_name):
        mongo_uri = f'mongodb://{host}:{port}'
        self.db = MongoClient(mongo_uri)[db_name]
        self.collection = self.db[collection_name]
        
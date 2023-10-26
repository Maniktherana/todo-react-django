from pymongo import MongoClient, ReturnDocument


class MongoConnection:
    def __init__(self, host, port, db_name, collection_name):
        mongo_uri = f"mongodb://{host}:{port}"
        self.db = MongoClient(mongo_uri)[db_name]
        self.collection = self.db[collection_name]

    def insert_one(self, document):
        return self.collection.insert_one(document)

    def find(self, query=None):
        if query is None:
            return self.collection.find()
        else:
            return self.collection.find(query)

    def find_one(self, query):
        return self.collection.find_one(query)

    def update_one(self, query, update):
        return self.collection.find_one_and_update(
            query, {"$set": update}, return_document=ReturnDocument.AFTER
        )

    def delete_one(self, query):
        return self.collection.delete_one(query)

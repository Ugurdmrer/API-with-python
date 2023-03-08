from pymongo import MongoClient



class dbConnection():
    
    def connection(self):
        client = MongoClient('localhost')
        db = client['database']
        collection = db['collection']
        cursor = collection.find()
        data = []
        for documents in cursor:
            data.append(documents)
        return data


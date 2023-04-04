import pymongo
import os
import json
from bson import json_util

class Mongo:
    """
    Mongo Class
    """
        
    client = pymongo.MongoClient()
    db = client[os.environ['mongo_db_name']]
    users_collection = db['users']

    def __init__(self):
        pass

    def retrieve_data(self) -> dict:
        """
        retrieve data from users collection
        """

        users = list(self.users_collection.find())

        return json.loads(json_util.dumps(users))

    def store_data(self, data: list):
        """
        store data in users collection
        """

        self.users_collection.create_index('id', unique=True)

        for user_data in data:
            try:
                self.users_collection.insert_one(user_data)
            except:
                print('mongo_unique_constraint')
        



import os
from typing import Dict
import pymongo


class Database:
    URI = "mongodb://<dbuser>:<dbpassword>@ds019766.mlab.com:19766/heroku_s67w94x6"
    DATABASE = None

    @staticmethod
    def __init__(self):
        client = pymongo.MongoClient(self.URI)
        self.DATABASE = client.get_default_database()

    @staticmethod
    def insert(collection: str, data: Dict) -> None:
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection: str, query: Dict, data: Dict) -> None:
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].remove(query)

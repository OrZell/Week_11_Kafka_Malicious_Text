from pymongo import MongoClient
from dotenv import find_dotenv, load_dotenv
import os

class Fetcher:

    def __init__(self):
        load_dotenv(find_dotenv())
        self.AtlasUser = os.getenv('ATLAS_USER')
        self.AtlasPassword = os.getenv('ATLAS_PASSWORD')
        self.AtlasDB = os.getenv('ATLAS_DB')
        self.AtlasCollection = os.getenv('ATLAS_COLLECTION')
        self.AtlasConnectString = os.getenv('ATLAS_CONNECT_STRING')
        self.TheStatementToSortBy = 'CreateDate'
        self.connection = None
        self.TimePassed = 0

    def fetch_hundred(self) -> list:
        self.open_connection()
        documents = self.find_hundred_documents()
        self.increase_the_counter()
        self.close_connection()
        return documents

    def open_connection(self):
        if self.connection is None:
            self.connection = MongoClient(self.AtlasConnectString)
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()
        self.connection = None

    def find_hundred_documents(self) -> list:
        connection = self.connection
        sort_by = self.TheStatementToSortBy

        how_many_times_did = self.TimePassed * 100
        cursor = connection[self.AtlasDB][self.AtlasCollection]

        documents = cursor.find().sort({sort_by:1}).limit(100).skip(how_many_times_did)
        return list(documents)

    def increase_the_counter(self):
        self.TimePassed += 1

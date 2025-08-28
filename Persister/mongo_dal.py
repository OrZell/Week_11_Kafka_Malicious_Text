from pymongo import MongoClient
from dotenv import find_dotenv, load_dotenv
import os


class MongoDal:

    def __init__(self):
        load_dotenv(find_dotenv())
        self.MongodbHost = os.getenv('LOCAL_MONGODB_HOST')
        self.MongodbPort = os.getenv('LOCAL_MONGODB_PORT')
        self.MongodbDB = os.getenv('LOCAL_MONGODB_DB')
        self.MongodbAnitCollection = os.getenv('LOCAL_MONGODB_COLLECTION_ANTI')
        self.MongodbNotAnitCollection = os.getenv('LOCAL_MONGODB_COLLECTION_NOT_ANTI')
        self.ConnectString = os.getenv('LOCAL_MONGODB_CONNECT_STRING')

        self.connection = None

    def open_connection(self):
        if self.connection is None:
            self.connection = MongoClient(self.ConnectString)
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()


    def save_tweet(self, tweet_data):

        connection = self.open_connection()

        if tweet_data["topic"] == "enriched_preprocessed_tweets_antisemitic":
            connection[self.MongodbDB][self.MongodbAnitCollection].insert_one(tweet_data['value'])

        elif tweet_data["topic"] == "enriched_preprocessed_tweets_not_antisemitic":
            connection[self.MongodbDB][self.MongodbNotAnitCollection].insert_one(tweet_data['value'])

    def get_antisemitic_docs(self):
        connection = self.open_connection()
        antisemitic_docs = connection[self.MongodbDB][self.MongodbAnitCollection].find()
        antisemitic_docs = list(antisemitic_docs)
        for doc in antisemitic_docs:
            del doc["_id"]
        return antisemitic_docs

    def get_not_antisemitic_docs(self):
        connection = self.open_connection()
        not_antisemitic_docs = connection[self.MongodbDB][self.MongodbNotAnitCollection].find()
        not_antisemitic_docs = list(not_antisemitic_docs)
        for doc in not_antisemitic_docs:
            del doc['_id']
        return not_antisemitic_docs
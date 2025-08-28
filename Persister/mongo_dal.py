import pymongo
from pymongo.errors import PyMongoError


class MongoDal:

    def __init__(self,connection_string,db_name):

        try:
            self.client = pymongo.MongoClient(connection_string)
            self.db = self.client[db_name]
            self.antisemitic_collection = self.db['tweets_antisemitic']
            self.not_antisemitic_collection = self.db['tweets_not_antisemitic']

        except PyMongoError as e:
            self.client = None


    def save_tweet(self, tweet_data):
        if self.client is None:
            return None

        if tweet_data["topic"] == "'enriched_preprocessed_tweets_antisemitic'":
            self.antisemitic_collection.insert_one(tweet_data["value"])

        elif tweet_data["topic"] == "enriched_preprocessed_tweets_not_antisemitic":
            self.not_antisemitic_collection.insert_one(tweet_data["value"])


    def close_connection(self):
        if self.client is not None:
            self.client.close()
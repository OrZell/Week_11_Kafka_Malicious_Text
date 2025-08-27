from consumer_raw_tweets import GetData_raw_tweets
from kafka_models.kafka_producer import Producer
from processor import processor

class manger():
    def __init__(self):
        self.tweets_antisemitic = GetData_raw_tweets()
        self.processed_tweets = processor()
        self.producer_tweets = Producer()

        self.first_tweets = None
        self.preprocessed_tweets_antisemitic = None
        self.preprocessed_tweets_not_antisemitic = None


    def app(self):
        self.first_tweets = self.tweets_antisemitic.get_data()

        self.preprocessed_tweets_antisemitic = self.processed_tweets.process(self.first_tweets[0])
        self.preprocessed_tweets_not_antisemitic = self.processed_tweets.process(self.first_tweets[1])

        self.producer_tweets.publish_list_of_messages(self.preprocessed_tweets_antisemitic, 'preprocessed_tweets_antisemitic')
        self.producer_tweets.publish_list_of_messages(self.preprocessed_tweets_not_antisemitic, 'preprocessed_tweets_not_antisemitic')




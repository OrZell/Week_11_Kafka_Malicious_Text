from kafka_models.kafka_consumer import Consumer
from kafka_models.kafka_producer import Producer
from processor import processor



class GetData_raw_tweets:
   def __init__(self):
      self.consumer = Consumer()
      self.preprocessed_tweets_antisemitic = None
      self.preprocessed_tweets_not_antisemitic = None
      self.processed_tweets = processor()
      self.producer_tweets = Producer()

   def get_data(self):
      events = self.consumer.get_consumer_events(['raw_tweets_antisemitic', 'raw_tweets_not_antisemitic'])
      for event in events:
         message = self.consumer.convert_to_dct_of_topic_and_value(event)
         if message["topic"] == "raw_tweets_antisemitic":
            self.preprocessed_tweets_antisemitic = self.processed_tweets.process(message["value"])
            print(self.preprocessed_tweets_antisemitic)
            # self.producer_tweets.publish_list_of_messages(self.preprocessed_tweets_antisemitic,'preprocessed_tweets_antisemitic')
         elif message["topic"] == "raw_tweets_not_antisemitic":
            self.preprocessed_tweets_not_antisemitic = self.processed_tweets.process(message["value"])
            print(self.preprocessed_tweets_not_antisemitic)
            # self.producer_tweets.publish_list_of_messages(self.preprocessed_tweets_not_antisemitic,'preprocessed_tweets_not_antisemitic')


app = GetData_raw_tweets()
app.get_data()
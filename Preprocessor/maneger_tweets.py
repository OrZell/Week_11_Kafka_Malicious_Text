from kafka_models.kafka_consumer import Consumer
from kafka_models.kafka_producer import Producer
from processor import Processor



class Maneger:
   def __init__(self):
      self.consumer = Consumer()
      self.processed_tweets = Processor()
      self.producer_tweets = Producer()
      self.preprocessed_tweets_antisemitic = None
      self.preprocessed_tweets_not_antisemitic = None

   def run(self):
      topic_data = self.consumer.get_consumer_events(['raw_tweets_antisemitic', 'raw_tweets_not_antisemitic'])

      for event in topic_data:
         all_message = self.consumer.convert_to_dct_of_topic_and_value(event)
         if all_message["topic"] == "raw_tweets_antisemitic":
            self.preprocessed_tweets_antisemitic = self.processed_tweets.process(all_message["value"])
            print(self.preprocessed_tweets_antisemitic)
            self.producer_tweets.publish_list_of_messages(messages=self.preprocessed_tweets_antisemitic,topic='preprocessed_tweets_antisemitic')
         elif all_message["topic"] == "raw_tweets_not_antisemitic":
            self.preprocessed_tweets_not_antisemitic = self.processed_tweets.process(all_message["value"])
            print(self.preprocessed_tweets_not_antisemitic)
            self.producer_tweets.publish_list_of_messages(messages=self.preprocessed_tweets_not_antisemitic,topic='preprocessed_tweets_not_antisemitic')



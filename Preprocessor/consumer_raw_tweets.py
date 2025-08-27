from kafka_models.kafka_consumer import Consumer


class GetData_raw_tweets:
   def __init__(self):
      self.consumer = Consumer()

   def get_data(self):
      events = self.consumer.consumer_with_auto_commit(['raw_tweets_antisemitic', 'raw_tweets_not_antisemitic'])
      return list(events)
from kafka_models.kafka_consumer import Consumer

class EnricherConsumer:
    
    def __init__(self):
        self.Consumer = Consumer()
        
    def listen_to_producer(self):
        consumer = self.Consumer.get_consumer_events(['preprocessed_tweets_antisemitic', 'preprocessed_tweets_not_antisemitic'])
        # consumer = self.Consumer.get_consumer_events(['raw_tweets_antisemitic', 'raw_tweets_not_antisemitic'])
        for event in consumer:
            event = self.Consumer.convert_to_dct_of_topic_and_value(event)
            print(event)


et = EnricherConsumer()
et.listen_to_producer()
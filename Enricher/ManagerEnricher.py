from kafka_models.kafka_consumer import Consumer
from kafka_models.kafka_producer import Producer
from Enricher import Enricher


class ManagerEnricher:
    
    def __init__(self):
        self.Consumer = Consumer()
        self.Enricher = Enricher()
        self.Producer = Producer()
        
    def run(self):
        consumer = self.Consumer.get_consumer_events(['preprocessed_tweets_antisemitic', 'preprocessed_tweets_not_antisemitic'])
        for event in consumer:
            # print(event)
            # continue
            event = self.Consumer.convert_to_dct_of_topic_and_value(event)
            print(event)
            event = self.Enricher.do_all(event['value'])
            if event['Antisemitic']:
                self.Producer.publish_message(topic='enriched_preprocessed_tweets_antisemitic', message=event)
            else:
                self.Producer.publish_message(topic='enriched_preprocessed_tweets_not_antisemitic', message=event)
            self.Producer.get_producer_config().flush()
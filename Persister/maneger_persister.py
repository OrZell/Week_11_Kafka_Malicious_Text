from mongo_dal import MongoDal
from kafka_models.kafka_consumer import Consumer



class ManegerPersister:
    def __init__(self):
        self.consumer = Consumer()
        self.client = MongoDal()

    def run_persister_service(self):

        topic_data = self.consumer.get_consumer_events(['enriched_preprocessed_tweets_antisemitic', 'enriched_preprocessed_tweets_not_antisemitic'])

        for event in topic_data:
            # print(event)
            # continue
            all_message = self.consumer.convert_to_dct_of_topic_and_value(event)
            self.client.save_tweet(all_message)
        self.client.close_connection()

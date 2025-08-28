from kafka import KafkaProducer
from dotenv import find_dotenv, load_dotenv
import os
import json

class Producer:

    def __init__(self):
        load_dotenv(find_dotenv())
        self.Host = os.getenv('KAFKA_HOST')
        self.Port = os.getenv('KAFKA_PORT')
        self.URI = os.getenv('KAFKA_CONNECT_STRING')

    def publish_list_of_messages(self, messages, topic):
        for message in messages:
            self.publish_message(message=message, topic=topic)

    def publish_message(self, topic, message):
        producer = self.get_producer_config()
        # print(f'topic={topic} || message={message}')
        producer.send(topic=topic, value=message)
        producer.flush()

    def get_producer_config(self):
        producer = KafkaProducer(bootstrap_servers=[self.URI],
                                 value_serializer=lambda x:
                                  json.dumps(x).encode('utf-8'))
        return producer

    def publish_message_with_key(self, topic, key, message):
        producer = self.get_producer_config()
        producer.send(topic, key=key, value=message)








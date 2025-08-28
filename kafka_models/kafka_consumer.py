from dotenv import find_dotenv, load_dotenv
import os
from kafka import KafkaConsumer
import json

class Consumer:

    def __init__(self):
        load_dotenv(find_dotenv())
        self.Host = os.getenv('KAFKA_HOST')
        self.Port = os.getenv('KAFKA_PORT')
        self.URI = os.getenv('KAFKA_CONNECT_STRING')

    @staticmethod
    def convert_to_messages(events):
        messages = []
        for message in events:
            message = "%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                 message.offset, message.key,
                                                 message.value)
            messages.append(message)
        return messages

    @staticmethod
    def convert_to_dct_of_topic_and_value(event):
        message = {
            'topic': event.topic,
            'value': event.value
        }
        return message

    def get_consumer_events(self, topic):
        consumer = KafkaConsumer(*topic,
                                 group_id='my-group',
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                                 bootstrap_servers=[self.URI])

        # consumer_timeout_ms = 10000 optional

        return consumer


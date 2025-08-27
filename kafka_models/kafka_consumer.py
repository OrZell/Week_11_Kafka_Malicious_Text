# from kafka_models.configurations import HOST, PORT
from dotenv import find_dotenv, load_dotenv
import os
from kafka import KafkaConsumer
from datetime import datetime
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

    # def consumer_with_auto_commit(self, topic):
    #     events = self.get_consumer_events(topic)
    #     events = self.convert_to_messages(events)
    #     return events
    #
    # def add_timestamp(self, events):
    #     data_as_documents = []
    #     for event in events:
    #         document = {}
    #         document['message'] = event
    #         document['timestamp'] = self.timestamp()
    #         data_as_documents.append(document)
    #
    #     return data_as_documents
    #
    # def timestamp(self):
    #     return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_consumer_events(self, topic):
        consumer = KafkaConsumer(topic,
                                 group_id='my-group',
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                                 bootstrap_servers=[self.URI],
                                 consumer_timeout_ms=10000)
        return consumer
from Fetch_Data.Fetcher import Fetcher
from kafka_models.kafka_producer import Producer

class ManagerFetching:

    def __init__(self):
        self.Fetcher = Fetcher()
        self.Producer = Producer()

    def run(self):
        data = self.fetch_documents()
        data = self.remove_id_statement(data)
        self.convert_date_to_str(data)
        data = self.organize_the_data(data)
        self.publish_data(data)

    def fetch_documents(self):
        documents = self.Fetcher.fetch_hundred()
        return documents

    @staticmethod
    def organize_the_data(documents) -> dict:
        data = {
            'antisemitic':[],
            'not_antisemitic':[]
                }

        for document in documents:
            if document['antisemitic'] == 1:
                data['antisemitic'].append(document)
            else:
                data['not_antisemitic'].append(document)

        return data

    @staticmethod
    def remove_id_statement(documents) -> list:
        data = []
        for document in documents:
            doc_id = str(document['_id'])
            document['id'] = doc_id

            del document['TweetID']
            del document['_id']

            data.append(document)

        return data

    @staticmethod
    def convert_date_to_str(documents):
        for document in documents:
            document['createdate'] = document['CreateDate'].strftime("%m/%d/%Y, %H:%M:%S")
            document['original_text'] = document['text']
            document['antisemitic'] = document['Antisemitic']

            del document['CreateDate']
            del document['text']
            del document['Antisemitic']

    def publish_data(self, data:dict):
        antisemitic_data = data['antisemitic']
        not_antisemitic_data = data['not_antisemitic']
        print(data['antisemitic'])
        self.Producer.publish_list_of_messages(messages=antisemitic_data, topic='raw_tweets_antisemitic')
        self.Producer.publish_list_of_messages(messages=not_antisemitic_data, topic='raw_tweets_not_antisemitic')
        self.Producer.get_producer_config().flush()
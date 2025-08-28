from nltk.sentiment.vader import SentimentIntensityAnalyzer
from Preprocessor.processor import Processor
import nltk
import re


class Enricher:

    def __init__(self):
        self.Processor = Processor()
        nltk.download('vader_lexicon', quiet=True)

    def do_all(self, event):
        processed_text = self.get_processed_text(event)
        emotion = self.find_emotion_of_text(processed_text)
        emotion_as_string = self.stringing_the_score(emotion)
        guns = self.find_weapons_in_processed_text(processed_text)
        date = self.search_dates(processed_text)
        event['sentiment'] = emotion_as_string
        event['weapons_detected'] = guns
        event['relevant_timestamp'] = date
        event = self.reorder_the_data(event)
        return event


    @staticmethod
    def find_emotion_of_text(text:str) -> float:
        score = SentimentIntensityAnalyzer().polarity_scores(text)['compound']
        return score

    @staticmethod
    def stringing_the_score(num:float) -> str:
        if 1 >= num >= 0.5:
            return 'positive'
        elif 0.49 >= num >= -0.49:
            return 'neutral'
        else:
            return 'negative'

    @staticmethod
    def get_processed_text(event:dict) -> str:
        return event['clean_text']

    def find_weapons_in_processed_text(self, processed_text:str) -> list:
        weapons = []
        with open('weapon_list.txt', 'r') as file:
            weapons_from_file = self.Processor.process_text([line.rstrip() for line in file])
            file.close()
        splited_processed_text = processed_text.split()
        for weapon in weapons_from_file:
            if weapon in splited_processed_text:
                weapons.append(weapon)

        if len(weapons) == 0:
            return ''
        return weapons

    @staticmethod
    def search_dates(processed_text):
        dates = re.findall(r'\d{4}-\d{2}-\d{2}', processed_text)
        last_one = sorted(dates, reverse=True)

        if len(last_one) == 0:
            return ''
        return last_one[0]

    @staticmethod
    def reorder_the_data(message:dict):
        order_template = ['id', 'createdate', 'antisemitic', 'original_text', 'clean_text', 'sentiment', 'weapons_detected', 'relevant_timestamp']
        ordered_message = {key: message[key] for key in order_template}
        return ordered_message

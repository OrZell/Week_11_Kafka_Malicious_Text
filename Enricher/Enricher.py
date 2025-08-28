from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import re


class Enricher:

    def __init__(self):
        nltk.download('vader_lexicon', quit=True)

    def run(self):


    @staticmethod
    def find_emotion_of_text(event:dict) -> float:
        text = event['processed_text']
        score = SentimentIntensityAnalyzer().polarity_scores(text)['compound']
        return score

    @staticmethod
    def stringing_the_score(num:int) -> str:
        if 1 >= num >= 0.5:
            return 'positive'
        elif 0.49 >= num >= -0.49:
            return 'neutral'
        else:
            return 'negative'

    @staticmethod
    def get_processed_text(event:dict) -> str:
        return event['processed_text']

    def clean_text(self, text:str):
        text = text.lower()
        for i in text:
            if i not in 'abcdefghijklmnopqrstuvwxyz1234567890':
                text.replace(i, '')
        return text


    def find_weapons_in_processed_text(self, processed_text:str) -> list:
        weapons = []
        with open('weapon_list.txt', 'r') as file:
            weapons_from_file = [self.clean_text(line.rstrip()) for line in file]
            file.close()
        splited_processed_text = processed_text.split()
        for weapon in weapons_from_file:
            if weapon in splited_processed_text:
                weapons.append(weapon)

        return weapons

    def search_dates(self, processed_text):
        dates = re.findall(r'\d{4}-\d{2}-\d{2}', processed_text)
        last_one = sorted(dates, reverse=True)
        return last_one


import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class Processor:

    def __init__(self):
        nltk.download('stopwords', quiet=True)
        nltk.download('wordnet', quiet=True)
        self.stopwords = stopwords.words('english')
        self.lemmatizer = WordNetLemmatizer()


    def process(self, item):

        text = item['text'].lower()
        text = re.sub(r'[^a-z0-9\s]', '', text)
        text = ' '.join(text.split())
        words = text.split()
        processed_words = []
        for word in words:
           if word not in self.stopwords:
              processed_words.append(self.lemmatizer.lemmatize(word))
              processed_text = ' '.join(processed_words)
              item['processed_text'] = processed_text

        return item








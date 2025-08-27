import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class processor:

    def __init__(self):
        nltk.download('stopwords')
        nltk.download('wordnet')
        self.stopwords = stopwords.words('english')
        self.lemmatizer = WordNetLemmatizer()


    def process(self, tweets):
        for item in tweets:
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

        return tweets








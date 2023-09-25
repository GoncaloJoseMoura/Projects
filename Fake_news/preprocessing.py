import pandas as pd
import numpy as np

import re
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

from sklearn.base import TransformerMixin, BaseEstimator

class Preprocessing_text(BaseEstimator, TransformerMixin):
    
    def fit(self, X, y = None):
        return self
        
    def transform(self, X):
        X = X.copy()
        
        X = X.fillna({'title': 'no title', 'author': 'no author'})
        X['text'] = X['title'] + ' by ' + X['author']
        
        return X['text']

# cleans (removes symbols, punctuation, emojis, stopwords and stems the words) and tokenizes our textual data
stop_words = stopwords.words('english')
ss = SnowballStemmer(language='english')

def f_tokenizer(x):
    cleaned_text = re.sub(r'[^a-zA-Z0-9 ]+', ' ', x) # removes all the symbols, emojis, punctuation marks
    tokens = cleaned_text.split() # splits on whitespaces
    remove_stopwords = [ss.stem(word) for word in tokens if tokens not in stop_words] # removes stopwords and stemms them
    
    return remove_stopwords
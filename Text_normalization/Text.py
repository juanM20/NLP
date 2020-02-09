import nltk
import re
import string
from bs4 import BeautifulSoup
from nltk.corpus import wordnet
from nltk import word_tokenize


def remove_char_2(tokens):
   
    for token in tokens:
        rep = re.sub(PATTERN, r' ', token)
        token = rep
    return tokens


def remove_characters_after_tokenization(tokens):
    pattern = re.compile('[{}]'.format(re.escape(string.punctuation))) 
    filtered_tokens = filter(None, [pattern.sub('', token) for token in tokens]) 
    return filtered_tokens



def remove_stopwords(tokens):
    stopword_list = nltk.corpus.stopwords.words('spanish')
    filtered_tokens = [token for token in tokens if token not in stopword_list]
    return filtered_tokens


if __name__ == '__main__':
    
    f = open('e961024.htm')
    text = f.read()
    f.close()

    soup = BeautifulSoup(text, 'lxml')
    text = soup.get_text()

    token_list = word_tokenize(text)
   
    filter1 = remove_characters_after_tokenization(token_list)
    filter_1 = list(filter1)
    
    filter_2 = sorted(list(set(filter_1)))
    
    filter_3 = remove_stopwords(filter_2)
   
    
    PATTERN = r'[^a-z]'

    filter_4 = [token for token in filter_3 if len(re.sub(PATTERN, r'', token)) > 0 ]
    print(filter_4)







    

    

    
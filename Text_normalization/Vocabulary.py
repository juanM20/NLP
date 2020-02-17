import nltk
import re
import string
from bs4 import BeautifulSoup
from nltk.corpus import wordnet
from nltk import word_tokenize


def remove_characters_after_tokenization(tokens):
    pattern = re.compile('[{}]'.format(re.escape(string.punctuation))) 
    filtered_tokens = filter(None, [pattern.sub('', token) for token in tokens]) 
    return filtered_tokens


def remove_characters_before_tokenization(token):
    
    PATTERN = r'\?|\$|&|\*|%|@|(|)|~|(-)|[0-9]|¿|¡|—|¦|º|”|;|,|\[|\]|\{|\}|#|:|\/|\\' # add other characters here to remove them
    filtered_sentence = re.sub(PATTERN, r'', token)

    return filtered_sentence



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

    token_list = word_tokenize(text.lower())
   
    filter1 = remove_characters_after_tokenization(token_list)
    filter_1 = list(filter1)
    
    filter_2 = list(set(filter_1))
        
    filter_3 = [remove_characters_before_tokenization(token) for token in filter_2 
                if len(remove_characters_before_tokenization(token)) > 0]
    
    filter_4 = remove_stopwords(filter_3)

    filter_5 = sorted(set(filter_4))
    
    #print(filter_5)
    print(len(filter_5))


    vocabulary = open('vocabulary.txt', 'w')
    for word in filter_5:
        vocabulary.write(word+'\n')
    vocabulary.close()








    

    

    
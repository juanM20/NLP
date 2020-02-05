import nltk
from nltk.corpus import brown

#print(brown.categories())
#print(brown.words(categories='news'))
#print(brown.words(fileids=['cg22']))
#print(brown.sents(categories=['news','editorial','reviews']))


news_text = brown.words(categories='news')
fdist = nltk.FreqDist([w.lower() for w in news_text])
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print('{}: {}'.format(m, fdist[m]))
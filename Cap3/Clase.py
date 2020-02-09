import nltk
from bs4 import BeautifulSoup

f = open('e961024.htm', encoding = 'utf-8')
text_string = f.read()
f.close()
# print(type(text))
# print(len(text))
# print(text[:1000])
# tokens = nltk.word_tokenize(text_string)
# text = nltk.Text(tokens)

# print(text[:100])

# print(text.concordance('actividad'))
# print(text.similar('actividad'))

soup = BeautifulSoup(text_string, 'lxml')
text_string = soup.get_text()

print(type(text_string))
print(len(text_string))

words = nltk.word_tokenize(text_string)

print(type(words))
print(len(words))
print(words[:200])


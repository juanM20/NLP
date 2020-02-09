from __future__ import division
import nltk, re, pprint

from urllib.request import urlopen
url = "http://www.gutenberg.org/files/30648/30648-h/30648-h.htm"
with urlopen(url) as res:
    raw = res.read()

print(type(raw))
print(len(raw))
print(raw[:75])

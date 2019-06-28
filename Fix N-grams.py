# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 09:32:07 2018

@author: Salman - Fix N-grams
"""
import csv
import nltk
import re
import bs4


import nltk.util.ngrams

from bs4 import BeautifulSoup, NavigableString
from soupselect import select
from nltk.corpus import stopwords
from collections import Counter
from nltk.tokenize import word_tokenize

non_speaker = re.compile('[A-Za-z]+: (.*)')

text = ' '.join(allData.Comment)

phrase_counter = Counter()
def extract_phrases(text, phrase_counter, length):
    for sent in nltk.sent_tokenize(text):
        strip_speaker = non_speaker.match(sent)
        if strip_speaker is not None:
            sent = strip_speaker.group(1)
        words = nltk.word_tokenize(sent)
        for phrase in nltk.util.ngrams(words, length):
            if all(word not in string.punctuation for word in phrase):
                phrase_counter[phrase] += 1
                
                
extract_phrases(text, phrase_counter, 3)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 14:23:41 2020

@author: oem
"""

#importing libraries
import nltk
from nltk.corpus import stopwords

#get the stop words for english
stop_words = set(stopwords.words('english'))
words_bryant = nltk.Text(nltk.corpus.gutenberg.words('bryant-stories.txt'))
words_emma = nltk.Text(nameltk.corpus.gutenberg.words('austen-emma.txt'))

#convert to small letters
words_bryant =  [word.lower() for word in words_bryant if word.isalpha()]
words_emma = [word.lower() for word in words_emma if word.isalpha()]

#remove stop words
words_bryant =  [word.lower() for word in words_bryant if word not in stop_words][:15000]
words_emma =    [word.lower() for word in words_emma if word not in stop_words][:15000]


TRR_bryant = len(set(words_bryant))/len(words_bryant)
TRR_emma = len(set(words_emma))/len(words_emma)


print('Number of tokens, Vocabulary, Type-emma ratio (Bryant Stories) = ',len(words_bryant),len(set(words_bryant)),TRR_bryant)


print('Number of tokens, Vocabulary, Type-emma ratio (Emma Stories) = ',len(words_emma),len(set(words_emma)),TRR_emma)

